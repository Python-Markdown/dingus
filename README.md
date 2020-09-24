# Python-Markdown Dingus

A simple site for testing Python-Markdown.
Visit <https://waylan.pythonanywhere.com/dingus> for a live demo.

 A backend which conforms to [Babelmark2]'s [API] is also provided at the URL: `/bablemark`.

[Babelmark2]: http://johnmacfarlane.net/babelmark2/
[API]: https://johnmacfarlane.net/babelmark2/faq.html#how-can-i-add-my-markdown-implementation-to-babelmark-2

# Setup

To set up a dev environment, clone this repo and create a virtual environment. Then
install the dependencies.

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

After a new release of Python-Markdown has been made, update with:

```bash
pip install -U markdown
```

# Running the server

To run a local instance of the server for development and testing:

```bash
python dingus.py
```

Then point your browser at <http://localhost:8080/dingus>.

To run a production instance you need to deploy a [bottle] server. For instance, to
configure a basic `wsgi` server, first ensure `dingus.py` is on your Python path. Then
create a `wsgi` configuration file as follows:

```python
import bottle
import dingus
application = bottle.default_app()
```

See the documentation for your specific server for instructions on pointing your server
at the `application` in your `wsgi` configuration file.

[bottle]: https://bottlepy.org/docs/dev/deployment.html

# Copyright

[Markdown] and [Dingus] Copyright &copy; 2004 [John Gruber]<br />
Additions and Modifications to Dingus (extension support, etc.)
Copyright &copy; 2012-2020 [Waylan Limberg]

[Markdown]: http://daringfireball.net/projects/markdown/
[Dingus]: http://daringfireball.net/projects/markdown/dingus
[John Gruber]: http://daringfireball.net/colophon/
[Waylan Limberg]: https://github.com/waylan
