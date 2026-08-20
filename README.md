# Python-Markdown Dingus

A simple site for testing Python-Markdown implemented as a [Cloudflare worker].
Visit <https://waylan.pythonanywhere.com/dingus> for a live demo.

A backend which conforms to [Babelmark3]'s [API] is also provided at the URL:
`/bablemark`.

[Cloudflare worker]: https://developers.cloudflare.com/workers/languages/python/
[Babelmark2]: https://babelmark.github.io/
[API]: https://github.com/babelmark/babelmark-registry

## Running the Cloudflare development server

To run a local instance of the server for development and testing, clone this
repo and run:

```bash
uv run pywrangler dev
```

Then point your browser at <http://127.0.0.1:8787/>.

For the Babelmark API, use <http://127.0.0.1:8787/babelmark?text=hi>.

## Running a simple development server

If you don't need the Babelmark backend and only want to use the webpage
frontend, you can run a simple server without any need for Cloudflare. The
webpage is a single page app which uses [Pyodide] to import and run
Python-Markdown within the browser locally.

You can run a simple static file server from the `public/` directory.

```bash
cd public/
python -m http.server
```

Then point your browser at <http://127.0.0.1:8000/>.

Any other static file server should work as well. There is no need for or
dependency on a local Python installation.

[Pyodide]: https://pyodide.org/en/stable/

## Copyright

[Markdown] and [Dingus] Copyright &copy; 2004 [John Gruber]<br />
Additions and Modifications to Dingus (extension support, etc.)
Copyright &copy; 2012-2026 [Waylan Limberg]

[Markdown]: http://daringfireball.net/projects/markdown/
[Dingus]: http://daringfireball.net/projects/markdown/dingus
[John Gruber]: http://daringfireball.net/colophon/
[Waylan Limberg]: https://github.com/waylan
