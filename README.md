fluffy-code
-----------

**fluffy-code** is a developer-friendly code rendering library for Python web
applications.

It can be used to easily render code with a bunch of user experience features
to help give your page a polished feel:


#### Syntax highlighting

![Syntax highlighting](https://i.fluffy.cc/msbDxbzG69pZCbjnhrk3qq7vmmnh8BSJ.png)


Syntax highlighting is backed by [Pygments](https://pygments.org/). fluffy-code
ships with two hand-picked color schemes, but you can swap those out for any
Pygments style.


#### Line highlighting

![Line highlighting](https://i.fluffy.cc/6CHS3hvqHjWJlslX20nDfr6qkGvpWck5.png)

Click the line numbers to highlight a line (or click-and-drag to highlight
multiple). The selected line numbers are automatically added to the URL's
fragment so that you can share your selection with others; when the URL is
loaded, the lines remain highlighted and the page scrolls down to the
selection.


#### Easy text selection and copy-paste

![Text selection](https://i.fluffy.cc/GXRPs3DPrsQWkthtnHt1wklzjT8H2fXV.png)

Code is rendered inside of a read-only but contenteditable container, which
makes it easy to select text. All of these options work:

* Click-and-drag inside the container to select text
* Right-click inside the text and click "select all" (it won't select the whole
  page, just the code!)
* Click inside the text and move your cursor around using arrow keys (you can
  use shift to select text, Ctrl-A to select all, etc)


#### Diff rendering

![Diff rendering](https://i.fluffy.cc/dCXrmKWl3N6nN631DJpWnt1LkrPMPtRP.png)

Code can be rendered in a special diff-aware mode where the text is still
syntax-highlighted using the regular Pygments lexer, but diff additions and deletions are
highlighted with a green or red background, similar to GitHub's diff viewer.


#### Terminal (ANSI) escape sequence rendering

![ANSI rendering](https://i.fluffy.cc/xQRXmZ1CHxWw90mDgQCdHq4lvFzwC8S3.png)

[pygments-ansi-color](https://github.com/chriskuehl/pygments-ansi-color) is
used to render output from terminals and color text according to ANSI escape
codes. This is useful when rendering terminal output which was piped into a
file to preserve the original color and styling. 8-color, 256-color, and
dim/bold modes are all supported.


#### Theme support

![Themes](https://i.fluffy.cc/pfQ3bsTFl7H0s9BrDRvLHPD35X3JzJ40.png)

All colors are fully themeable, and users can swap between the themes
clientside. fluffy-code ships with one light theme (the default) and one dark
theme, but new themes are as easy as picking a Pygments style and defining a
few matching colors for the line numbers.


## Sounds great! Where can I try it out?

Here are a few samples of fluffy-code text rendered via
[fluffy](https://github.com/chriskuehl/fluffy), a pastebin-type app where this
library originated:

* [A simple Python script with syntax highlighting](https://i.fluffy.cc/cxGSDD5JcC8g6Lm3L1VngbmNJZDRR4Bm.html)
* [A diff of a Python script with diff highlights and syntax highlighting](https://i.fluffy.cc/rjX2XQDMhflK3ZDXJNwcBxpmNt8986Vh.html)
* [A snippet of terminal output with ANSI color code highlighting](https://i.fluffy.cc/cgQc0Wv7FtL6X1JLw5VbZ242bZ3BlGjq.html)

Make sure you play with the theme dropdown in the top-right to try it out with
different color schemes.

If you just want to see a few samples of fluffy-code snippets rendered in HTML
by themselves, check out [TODO: the auto-generated samples on GitHub Pages].


## Usage

Install `fluffy-code` via pip, then use code like this to generate HTML:

```python
import pygments.lexers
from fluffy_code import code
from fluffy_code import prebuilt_styles

markup = code.render(
    # Replace this with your text.
    "my python code",
    # You can replace this with `monokai_style()` for a dark theme, or create
    # your own theme with the instructions below.
    style_config=prebuilt_styles.default_style(),
    highlight_config=code.HighlightConfig(
        # Adjust lexer name as needed. Pygments also provides other options
        # such as guessing the lexer based on file extension or file contents.
        lexer=pygments.lexers.get_lexer_by_name('python'),
        # Set to True if you want to highlight additions and deletions for a diff.
        highlight_diff=False,
    ),
)
```

The returned object is an instance of `markupsafe.Markup` which can be rendered
in Jinja and most other templating systems directly. You can pass it to `str()`
if you just want the HTML as a string.


### Including required CSS and JavaScript

fluffy-code requires you to include a JavaScript snippet (for line number
highlighting to work) and some CSS styling. To get these, use:

```python
from fluffy_code import code
from fluffy_code import prebuilt_styles

# To get the global JavaScript.
print(code.get_global_javascript())

# To get the global CSS.
print(code.get_global_css())

# To get the CSS for a specific theme.
#
# These rules do not conflict, so you can include CSS for as many themes as
# you'd like on the same page and manipulate the CSS classes to swap between
# them clientside.
style = prebuilt_styles.default_style()
print(style.css)
```

You can integrate these into your build system and put them on your CDN at
build time, or include them in your HTML at runtime.

At the moment, you also need to include jQuery on your page for the JavaScript
to function. This is on the short-term roadmap to remove.


### Defining new themes

Defining new themes is easy; you just need to pick a [Pygments
style][pygments-styles] and then a few matching colors for the UI elements that
fluffy-code adds. For a full example, check out the [pre-built
themes][prebuilt-themes] that ship with fluffy-code. You can construct your own
`StyleConfig` objects in exactly the same way.


## Contributing

To build this project locally, you'll need to [install
Poetry](https://python-poetry.org/docs/) and run `poetry install`.

Once installed, you can run

```bash
$ poetry run python -m testing.generate_test_html
```

to generate a self-contained file named `test.html` using your current
checkout.


## Roadmap
### Short-term

* Remove requirement on jQuery
* Properly support multiple code views per page (currently it works fine except
  when selecting lines, since the selected lines are added to the URL's
  fragment component with no differentiation between which code view they are
  for)


[pygments-styles]: https://pygments.org/docs/styles/
[prebuilt-themes]: https://github.com/chriskuehl/fluffy-code/blob/main/fluffy_code/prebuilt_styles.py
[markupsafe]: https://markupsafe.palletsprojects.com/en/2.1.x/
