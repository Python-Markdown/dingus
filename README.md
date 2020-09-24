# Python-Markdown Dingus

A simple site for testing Python-Markdown as well as the backend called by [Babelmark].
Visit <https://waylan.pythonanywhere.com/dingus> for a live demo.

[Babelmark]: http://johnmacfarlane.net/babelmark2/

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

# Copyright and License

[Markdown] and [Dingus] Copyright &copy; 2004 [John Gruber]<br />
Additions and Modifications to Dingus (extension support, etc.) Copyright &copy; 2012-2020 [Waylan Limberg]

[Markdown]: http://daringfireball.net/projects/markdown/
[Dingus]: http://daringfireball.net/projects/markdown/dingus
[John Gruber]: http://daringfireball.net/colophon/
[Waylan Limberg]: https://github.com/waylan
