from bottle import route, run, request, template
import markdown
from markdown.extensions import extra
import os


# Get a list of markdown extensions
extensions = [ext.name for ext in markdown.util.INSTALLED_EXTENSIONS if ext.name not in extra.extensions + ['extra']]
extensions.sort()
extra.extensions.sort()

@route('/babelmark')
def babelmark():
    """ Provide a hook for http://johnmacfarlane.net/babelmark2/ to use. """
    src = request.query.get('text', '')
    return {
        'name'   : 'Python-Markdown',
        'version': markdown.version,
        'html'   : markdown.markdown(src)
    }

@route('/dingus', method=('GET', 'POST'))
def dingus():
    context = {'extensions': extensions, 'extra': extra.extensions}
    # Get data from GET or POST
    context['src'] = request.params.get('src', '')
    context['ext'] = request.params.getall('ext')
    context['output_format'] = request.params.get('output_format', '')
    # Build rest of context
    context['version'] = markdown.version
    # Build command
    cmd = 'markdown.markdown(src'
    if context['ext']:
        cmd += ', extensions={}'.format(context['ext'])
    if context['output_format']:
        cmd += ", output_format='{}'".format(context['output_format'])
    context['cmd'] = cmd + ')'
    # Convert
    kwargs = {'extensions': context['ext']}
    if context['output_format']: kwargs['output_format'] = context['output_format']
    context['result'] = markdown.markdown(context['src'], **kwargs)
    return template(tmpl, **context)


tmpl = """<!doctype html>
<html>
  <head>
    <title>Python-Markdown: Dingus</title>
    <meta charset="UTF-8"/>
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/styles/github.min.css">
    <style type="text/css">
    /*
    	Basic layout courtesy of InkNoise's very nifty Layout-o-matic:
		http://www.inknoise.com/experimental/layoutomatic.php
	*/

	#sidebar h1 {
		font-size: 1.5em;
		font-weight: bold;
	}
	#sidebar h2 {
		font-size: 1.2em;
		font-weight: bold;
		margin-bottom: -.5em;
	}
	#sidebar h3 {
		font-size: 1em;
		font-weight: bold;
		text-transform: none;
		margin-bottom: .25em;
		margin-top: 1.5em;
	}
	#sidebar code {
		font-family: Monaco, ProFont, "Andale Mono", "Lucida Console", Courier, monospace;
		font-size: 10px;
	}
	#sidebar pre {
		line-height: 12px;
		margin-top: 0;
		background-color: #f5f5f5;
		border: 1px solid #ccc;
		padding: 4px;
	}
	#sidebar p {
		margin-top: 0;
		margin-bottom: 0;
	}

	body {
		background-color: #eee;
		font-family: "Lucida Grande", Verdana, sans-serif;
		font-size: 11px;
		line-height: 1.6em;
	}
	.renderbox {
		background: white;
		font-family: Georgia, serif;
		font-size: 13px;
		border: 1px #888 solid;
		padding: 0 5px;
		margin: 0;
		width: 97%;
		overflow: auto;
	}
    div.codehilite pre code, pre.renderbox code {
        background: transparent;
    }
	.label {
		margin-bottom: 4px;
	}

	#container {
		border: 0px solid gray;
		margin: 10px;
		margin-left: auto;
		margin-right: auto;
		padding: 0px;
		min-width: 750px;

		/* For Win/IE: */
		width:expression("800px" );
		margin-left:expression("0");
	}

	#banner {
		padding: 0;
		margin-bottom: 5px;
		background-color: transparent;
	}

	#app {
		padding: 0 10px 0 10px;
		margin-right: 270px;
		background-color: transparent;
		border-right: 0px solid #bbb;
	}

	#sidebar {
		float: right;
		width: 250px;
		margin: 0;
		margin-right: 10px;
		padding: 0;
		background-color: transparent;
	}

	.footer {
		margin-top: 100px;
	}

	#buttonrow {
		margin-top: 10px;
		margin-bottom: 60px;
	}
	#convert {
		width: 7em;
		margin-left:20px;
	}

	textarea[name="src"] {
	/* WinIE is retarded. Thanks to Sam Ruby for the workaround:
		http://www.intertwingly.net/blog/1432.html */
		width: 98%;
	}

	</style>

    <style>
    .codehilite code { background-color: #ffffcc }
    .codehilite .hll { background-color: #ffffcc }
    .codehilite  { background: #f0f0f0; }
    .codehilite .c { color: #60a0b0; font-style: italic } /* Comment */
    .codehilite .err { border: 1px solid #FF0000 } /* Error */
    .codehilite .k { color: #007020; font-weight: bold } /* Keyword */
    .codehilite .o { color: #666666 } /* Operator */
    .codehilite .cm { color: #60a0b0; font-style: italic } /* Comment.Multiline */
    .codehilite .cp { color: #007020 } /* Comment.Preproc */
    .codehilite .c1 { color: #60a0b0; font-style: italic } /* Comment.Single */
    .codehilite .cs { color: #60a0b0; background-color: #fff0f0 } /* Comment.Special */
    .codehilite .gd { color: #A00000 } /* Generic.Deleted */
    .codehilite .ge { font-style: italic } /* Generic.Emph */
    .codehilite .gr { color: #FF0000 } /* Generic.Error */
    .codehilite .gh { color: #000080; font-weight: bold } /* Generic.Heading */
    .codehilite .gi { color: #00A000 } /* Generic.Inserted */
    .codehilite .go { color: #808080 } /* Generic.Output */
    .codehilite .gp { color: #c65d09; font-weight: bold } /* Generic.Prompt */
    .codehilite .gs { font-weight: bold } /* Generic.Strong */
    .codehilite .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
    .codehilite .gt { color: #0040D0 } /* Generic.Traceback */
    .codehilite .kc { color: #007020; font-weight: bold } /* Keyword.Constant */
    .codehilite .kd { color: #007020; font-weight: bold } /* Keyword.Declaration */
    .codehilite .kn { color: #007020; font-weight: bold } /* Keyword.Namespace */
    .codehilite .kp { color: #007020 } /* Keyword.Pseudo */
    .codehilite .kr { color: #007020; font-weight: bold } /* Keyword.Reserved */
    .codehilite .kt { color: #902000 } /* Keyword.Type */
    .codehilite .m { color: #40a070 } /* Literal.Number */
    .codehilite .s { color: #4070a0 } /* Literal.String */
    .codehilite .na { color: #4070a0 } /* Name.Attribute */
    .codehilite .nb { color: #007020 } /* Name.Builtin */
    .codehilite .nc { color: #0e84b5; font-weight: bold } /* Name.Class */
    .codehilite .no { color: #60add5 } /* Name.Constant */
    .codehilite .nd { color: #555555; font-weight: bold } /* Name.Decorator */
    .codehilite .ni { color: #d55537; font-weight: bold } /* Name.Entity */
    .codehilite .ne { color: #007020 } /* Name.Exception */
    .codehilite .nf { color: #06287e } /* Name.Function */
    .codehilite .nl { color: #002070; font-weight: bold } /* Name.Label */
    .codehilite .nn { color: #0e84b5; font-weight: bold } /* Name.Namespace */
    .codehilite .nt { color: #062873; font-weight: bold } /* Name.Tag */
    .codehilite .nv { color: #bb60d5 } /* Name.Variable */
    .codehilite .ow { color: #007020; font-weight: bold } /* Operator.Word */
    .codehilite .w { color: #bbbbbb } /* Text.Whitespace */
    .codehilite .mf { color: #40a070 } /* Literal.Number.Float */
    .codehilite .mh { color: #40a070 } /* Literal.Number.Hex */
    .codehilite .mi { color: #40a070 } /* Literal.Number.Integer */
    .codehilite .mo { color: #40a070 } /* Literal.Number.Oct */
    .codehilite .sb { color: #4070a0 } /* Literal.String.Backtick */
    .codehilite .sc { color: #4070a0 } /* Literal.String.Char */
    .codehilite .sd { color: #4070a0; font-style: italic } /* Literal.String.Doc */
    .codehilite .s2 { color: #4070a0 } /* Literal.String.Double */
    .codehilite .se { color: #4070a0; font-weight: bold } /* Literal.String.Escape */
    .codehilite .sh { color: #4070a0 } /* Literal.String.Heredoc */
    .codehilite .si { color: #70a0d0; font-style: italic } /* Literal.String.Interpol */
    .codehilite .sx { color: #c65d09 } /* Literal.String.Other */
    .codehilite .sr { color: #235388 } /* Literal.String.Regex */
    .codehilite .s1 { color: #4070a0 } /* Literal.String.Single */
    .codehilite .ss { color: #517918 } /* Literal.String.Symbol */
    .codehilite .bp { color: #007020 } /* Name.Builtin.Pseudo */
    .codehilite .vc { color: #bb60d5 } /* Name.Variable.Class */
    .codehilite .vg { color: #bb60d5 } /* Name.Variable.Global */
    .codehilite .vi { color: #bb60d5 } /* Name.Variable.Instance */
    .codehilite .il { color: #40a070 } /* Literal.Number.Integer.Long */
    </style>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/highlight.min.js"></script>
    <script type="text/javascript">
      $(document).ready(function(){
        // JS is active, so setup for it.
        $("#extensions").hide();
        var showExt = true;
        $("#toggle_ext").show();
        if ($("#extra input").is(":checked")) {
          $("#extra-exts").find(':input:not(:disabled)').prop('disabled',true);
        };

        // Highlight "HTML Source" and "Python Code" - but not "HTML Preview" or cheatsheet blocks.
        // If codehilite is used, that highlight codeblocks in the preview seperately.
        $("pre.renderbox code").each(function(i, e) {hljs.highlightBlock(e)});

        // Bind toggle click
        $("#toggle_ext").click(function(event){
          if (showExt == true) {
            $("#extensions").slideDown("fast");
            $(event.target).text("Hide Extensions ^");
            showExt = false;
          } else if (showExt == false) {
            $("#extensions").slideUp("fast");
            $(event.target).text("Show Extensions v");
            showExt = true;
          };
          event.preventDefault();
        });

        // Bind Extra input change
        $("#extra input").change(function(event){
          if (event.target.checked == true) {
            $("#extra-exts").find(':input:not(:disabled)').prop('disabled',true);
          } else if (event.target.checked == false) {
            $("#extra-exts").find(':input:disabled').prop('disabled',false);
          };
        });

      });
    </script>
  </head>
  <body>

<div id="container">

<div id="sidebar">
<h1>Python-Markdown: Dingus</h1>

<h2>Syntax Cheatsheet:</h2>

<h3>Phrase Emphasis</h3>

<pre><code>*italic*   **bold**
_italic_   __bold__
</code></pre>

<h3>Links</h3>

<p>Inline:</p>

<pre><code>An [example](http://url.com/ "Title")
</code></pre>

<p>Reference-style labels (titles are optional):</p>

<pre><code>An [example][id]. Then, anywhere
else in the doc, define the link:

  [id]: http://example.com/  "Title"
</code></pre>

<h3>Images</h3>

<p>Inline (titles are optional):</p>

<pre><code>![alt text](/path/img.jpg "Title")
</code></pre>

<p>Reference-style:</p>

<pre><code>![alt text][id]

[id]: /url/to/img.jpg "Title"
</code></pre>

<h3>Headers</h3>

<p>Setext-style:</p>

<pre><code>Header 1
========

Header 2
--------
</code></pre>

<p>atx-style (closing #'s are optional):</p>

<pre><code># Header 1 #

## Header 2 ##

###### Header 6
</code></pre>

<h3>Lists</h3>

<p>Ordered, without paragraphs:</p>

<pre><code>1.  Foo
2.  Bar

</code></pre>

<p>Unordered, with paragraphs:</p>

<pre><code>*   A list item.

    With multiple paragraphs.

*   Bar
</code></pre>

<p>You can nest them:</p>

<pre><code>*   Abacus
    * answer
*   Bubbles
    1.  bunk
    2.  bupkis
        * BELITTLER
    3. burper
*   Cunning
</code></pre>

<h3>Blockquotes</h3>

<pre><code>&gt; Email-style angle brackets
&gt; are used for blockquotes.

&gt; &gt; And, they can be nested.

&gt; #### Headers in blockquotes
&gt;
&gt; * You can quote a list.
&gt; * Etc.
</code></pre>

<h3>Code Spans</h3>

<pre><code>`&lt;code&gt;` spans are delimited
by backticks.

You can include literal backticks
like `` `this` ``.
</code></pre>

<h3>Preformatted Code Blocks</h3>

<p>Indent every line of a code block by at least 4 spaces or 1 tab.</p>

<pre><code>This is a normal paragraph.

    This is a preformatted
    code block.
</code></pre>

<h3>Horizontal Rules</h3>

<p>Three or more dashes or asterisks:</p>

<pre><code>---

* * *

- - - -
</code></pre>

<h3>Manual Line Breaks</h3>

<p>End a line with two or more spaces:</p>

<pre><code>Roses are red,
Violets are blue.
</code></pre>
</div> <!-- sidebar -->

<div id="app">

    <form action="/dingus" method="post">
      <div id="src">
        <p class="label">Markdown Source:</p>
        <textarea name="src"  rows="25" cols="80">{{ src }}</textarea>
      </div> <!-- src -->

      <div id="buttonrow">

      <fieldset id="extensions">
        <legend>Extensions</legend>
%for x in extensions:
        <label id="{{ x }}"><input type="checkbox" name="ext" value="{{ x }}"\\\\
%if x in ext:
 checked\\\\
%end
 /><code>{{ x }}</code></label>
%end
        <fieldset>
        <legend><label id="extra"><input type="checkbox" name="ext" value="extra"\\\\
%if "extra" in ext:
 checked\\\\
%end
 /><code>extra</code></label></legend>

      <div id="extra-exts">
%for x in extra:
        <label id="{{ x }}"><input type="checkbox" name="ext" value="{{ x }}"\\\\
%if x in ext:
 checked\\\\
%end
 /><code>{{ x }}</code></label>
%end
      </div> <!-- extra-exts -->
      </fieldset>
      </fieldset> <!-- extensions -->

      <a href="#" id="toggle_ext" style="display:none">Show Extensions v</a>


      <label id="output_format">Output_Format:
        <select name="output_format" value="{{ output_format }}">
          <option value="">xhtml (default)</option>
          <option value="html"\\\\
%if output_format == "html":
 selected="selected"\\\\
%end
>html</option>
        </select>
      </label>

      <input type="submit" id="convert" value="Convert" />
      </div> <!--buttonrow-->

    </form>
%if result:
    <p class="label">HTML Source:</p>
    <pre id="rawoutput" class="renderbox"><code class="html">{{ result }}</code></pre>

    <p class="label">HTML Preview:</p>
    <div id="output" class="renderbox">
      {{! result }}
    </div>

    <p class="label">Python Code:</p>
    <pre id="python" class="renderbox"><code class="python">import markdown
html = {{ cmd }}</code></pre>
%end

<p class='footer'>
  <a href="https://python-markdown.github.io/">Python-Markdown</a> version {{ version }}<br />
  Copyright &copy; 2007-2020 Python-Markdown Project (v. 1.7 and later)<br />
  Copyright &copy; 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)<br />
  Copyright &copy; 2004 Manfred Stienstra (the original version)<br />
  <br />
  <a href="http://daringfireball.net/projects/markdown/">Markdown</a> and
  <a href="http://daringfireball.net/projects/markdown/dingus">Dingus</a> Copyright &copy; 2004
  <a href="http://daringfireball.net/colophon/">John Gruber</a><br />
  Additions and Modifications to Dingus (extension support, etc.) Copyright &copy; 2012-2020
  <a href="https://github.com/waylan">Waylan Limberg</a>

</p>

</div> <!-- app -->
</div> <!-- container -->

  </body>
</html>
"""


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
