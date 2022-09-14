import importlib.resources
import typing

import pygments.lexer
import pygments.lexers.special
from markupsafe import Markup
from pyquery import PyQuery as pq  # type: ignore

from fluffy_code.style import StyleConfig


class HighlightConfig(typing.NamedTuple):
    lexer: pygments.lexer.Lexer
    highlight_diff: bool

    def highlight(self, text: str, style_config: StyleConfig) -> str:
        highlighted = pygments.highlight(
            text,
            self.lexer,
            formatter=style_config.pygments_formatter,
        )

        if self.highlight_diff:
            html = pq(highlighted)
            lines = html('pre > span')

            # there's an empty span at the start...
            assert 'id' not in lines[0].attrib
            pq(lines[0]).remove()
            lines.pop(0)

            for line in lines:
                line = pq(line)
                assert line.attr('id').startswith('line-')

                el = pq(line)

                # .text() doesn't include whitespace before it, but .html() does
                h = el.html()
                text = h[:len(h) - len(h.lstrip())] + el.text()

                if text.startswith('+'):
                    line.addClass('diff-add')
                elif text.startswith('-'):
                    line.addClass('diff-remove')

            return html.outerHtml()
        else:
            return highlighted


def get_global_css() -> str:
    return importlib.resources.read_text('fluffy_code.static', 'global.css')


def get_global_javascript() -> str:
    return importlib.resources.read_text('fluffy_code.static', 'global.js')


def render(
    text: str,
    *,
    style_config: StyleConfig,
    highlight_config: HighlightConfig:
) -> Markup:
    line_count = len(text.splitlines())

    highlighted = highlight_config.highlight(
        text,
        style_config,
    )

    line_numbers = Markup('<div class="line-numbers">{}</div>').format(
        Markup('').join(
            # TODO: don't use id in order to support multiple per page
            Markup('<a id={}>{}</a>').format(
                f'LL{i}',
                i,
            )
            for i in range(1, line_count + 1)
        ),
    )

    code = Markup("""
        <div class="text" contenteditable="true" spellcheck="false">
            {highlighted}
        </div>
    """).format(
        highlighted=Markup(highlighted),
    )

    return Markup('<div class="fluffy-code {class_}">{line_numbers}{code}</div>').format(
        class_=f'highlight-{style_config.name}',
        line_numbers=line_numbers,
        code=code,
    )
