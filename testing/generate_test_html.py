import typing

import pygments.lexers
from markupsafe import Markup

from fluffy_code import code
from fluffy_code import prebuilt_styles


def main() -> typing.Optional[int]:
    style_config_default = prebuilt_styles.default_style()
    style_config_monokai = prebuilt_styles.monokai_style()

    python_code = code.render(
        open('testing/samples/python.py').read(),
        style_config=style_config_default,
        highlight_config=code.HighlightConfig(
            lexer=pygments.lexers.get_lexer_by_name('python'),
            highlight_diff=False,
        ),
    )

    diff_python = code.render(
        open('testing/samples/python.diff').read(),
        style_config=style_config_default,
        highlight_config=code.HighlightConfig(
            lexer=pygments.lexers.get_lexer_by_name('python'),
            highlight_diff=True,
        ),
    )

    ansi_color = code.render(
        open('testing/samples/ansi-color').read(),
        style_config=style_config_monokai,
        highlight_config=code.HighlightConfig(
            lexer=pygments.lexers.get_lexer_by_name('ansi-color'),
            highlight_diff=False,
        ),
    )

    page = Markup("""
    <!doctype html>
    <html>
        <head>
            <style>{css}</style>
        </head>

        <body>
            <h2>Python code</h2>
            {python_code}

            <h2>Diff (python)</h2>
            {diff_python}

            <h2>ANSI color + monokai</h2>
            {ansi_color}

            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
            <script>{javascript}</script>
        </body>
    </html>
    """).format(
        css=Markup(
            '\n'.join((
                code.get_global_css(),
                style_config_default.css,
                style_config_monokai.css,
            )),
        ),
        javascript=Markup(code.get_global_javascript()),
        python_code=Markup(python_code),
        diff_python=Markup(diff_python),
        ansi_color=Markup(ansi_color),
    )

    with open('test.html', 'w') as f:
        f.write(page)


if __name__ == '__main__':
    raise SystemExit(main())
