from pygments.token import Token


def test_pygments_ansi_color_tokens(default_style):
    assert Token.C.Red in default_style.pygments_formatter.style.styles


def test_css(default_style):
    assert ".highlight-default .line-numbers {" in default_style.css
