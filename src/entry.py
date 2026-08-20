from workers import Response, WorkerEntrypoint
from urllib.parse import urlsplit, parse_qsl
import markdown

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        url = urlsplit(request.url)
        if url.path == '/babelmark':
            querystr = dict(parse_qsl(url.query))
            src = querystr.get('text', '')
            data = {
                'name'   : 'Python-Markdown',
                'version': markdown.__version__,
                'html'   : markdown.markdown(src)
            }
            return Response.json(data)
        return Response('Not Found', status=404)
