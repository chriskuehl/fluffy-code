import pygments.lexers.python
import pygments.lexers.special
import pytest
from markupsafe import Markup
from pyquery import PyQuery

from fluffy_code import code


def test_get_global_css():
    assert '.fluffy-code {' in code.get_global_css()


def test_get_global_javascript():
    assert '$(document).ready(' in code.get_global_javascript()


def test_highlight_config_does_not_allow_lexer_with_stripnl_enabled():
    with pytest.raises(AssertionError) as exc_info:
        code.HighlightConfig(
            lexer=pygments.lexers.special.TextLexer(),
            highlight_diff=False,
        )
    assert (
        'Cannot construct HighlightConfig using a Pygments lexer with stripnl not set to False'
        in exc_info.value.args[0]
    )


def test_render_plain_text(default_style):
    rendered = code.render(
        'simple line of text',
        style_config=default_style,
        highlight_config=code.HighlightConfig(
            lexer=pygments.lexers.special.TextLexer(stripnl=False),
            highlight_diff=False,
        ),
    )
    assert isinstance(rendered, Markup)
    html = str(rendered)
    assert html.startswith('<div class="fluffy-code highlight-default">')
    assert 'simple line of text' in html


def test_render_python_diff(default_style):
    rendered = code.render(
        (
            ' def foo():\n'
            '-    return "a"\n'
            '+    return "b"'
        ),
        style_config=default_style,
        highlight_config=code.HighlightConfig(
            lexer=pygments.lexers.python.PythonLexer(stripnl=False),
            highlight_diff=True,
        ),
    )
    assert isinstance(rendered, Markup)
    html = str(rendered)
    pq = PyQuery(html)
    assert pq('.diff-remove').text() == '- return "a"'
    assert pq('.diff-add').text() == '+ return "b"'
