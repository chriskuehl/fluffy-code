import typing
from dataclasses import dataclass

import pygments.formatters
import pygments.style
import pygments.styles.xcode
import pygments_ansi_color


class FluffyCodeFormatter(
    pygments_ansi_color.ExtendedColorHtmlFormatterMixin,
    pygments.formatters.HtmlFormatter,
):
    pass


@dataclass(frozen=True)
class StyleConfig:
    """Represents a single set of colors, fonts, etc. to use for displaying code.

    Each StyleConfig is one specific way of rendering code. If you want to
    offer multiple sets of style options (e.g. a light mode and a dark mode),
    you should create one StyleConfig for each.

    Normally you should instantiate this using the `from_pygments_style`
    method since it does some special setup on the pygments style for
    pygments_ansi_color compatibility.
    """
    name: str
    pygments_formatter: pygments.formatter.Formatter
    border_color: str
    line_numbers_fg_color: str
    line_numbers_bg_color: str
    line_numbers_hover_bg_color: str
    line_numbers_selected_bg_color: str
    selected_line_bg_color: str
    diff_add_line_bg_color: str
    diff_add_selected_line_bg_color: str
    diff_delete_line_bg_color: str
    diff_delete_selected_line_bg_color: str

    @classmethod
    def from_pygments_style(
        cls,
        *,
        name: str,
        pygments_style: typing.Type[pygments.style.Style],
        ansi_fg_colors: typing.Dict[str, str],
        ansi_bg_colors: typing.Dict[str, str],
        border_color: str,
        line_numbers_fg_color: str,
        line_numbers_bg_color: str,
        line_numbers_hover_bg_color: str,
        line_numbers_selected_bg_color: str,
        selected_line_bg_color: str,
        diff_add_line_bg_color: str,
        diff_add_selected_line_bg_color: str,
        diff_delete_line_bg_color: str,
        diff_delete_selected_line_bg_color: str,
    ) -> 'StyleConfig':
        """Create StyleConfig from a classic Pygments style.

        This takes care of configuring the style for compatibility with
        pygments_ansi_color.
        """
        new_styles = dict(pygments_style.styles)  # type: ignore
        new_styles.update(
            pygments_ansi_color.color_tokens(
                ansi_fg_colors,
                ansi_bg_colors,
                enable_256color=True,
            ),
        )
        new_pygments_style = type(
            'FluffyCode' + pygments_style.__name__,  # type: ignore
            (pygments_style,),
            {'styles': new_styles},
        )

        return cls(
            name=name,
            pygments_formatter=FluffyCodeFormatter(
                noclasses=False,
                linespans='line',
                style=new_pygments_style,
            ),
            border_color=border_color,
            line_numbers_fg_color=line_numbers_fg_color,
            line_numbers_bg_color=line_numbers_bg_color,
            line_numbers_hover_bg_color=line_numbers_hover_bg_color,
            line_numbers_selected_bg_color=line_numbers_selected_bg_color,
            selected_line_bg_color=selected_line_bg_color,
            diff_add_line_bg_color=diff_add_line_bg_color,
            diff_add_selected_line_bg_color=diff_add_selected_line_bg_color,
            diff_delete_line_bg_color=diff_delete_line_bg_color,
            diff_delete_selected_line_bg_color=diff_delete_selected_line_bg_color,
        )

    @property
    def css(self) -> str:
        prefix = f'.highlight-{self.name}'
        css = self.pygments_formatter.get_style_defs(f'{prefix} .highlight')
        css += f"""
            {prefix} .line-numbers {{
              background-color: {self.line_numbers_bg_color};
              border-color: {self.border_color};
            }}
            {prefix} .text {{
              background-color: {self.border_color};
            }}
            {prefix} .line-numbers a {{
              color: {self.line_numbers_fg_color};
            }}
            {prefix} .line-numbers a:hover {{
              background-color: {self.line_numbers_hover_bg_color} !important;
            }}
            {prefix} .line-numbers a.selected {{
              background-color: {self.line_numbers_selected_bg_color};
            }}
            {prefix} .text .highlight > pre > span.selected {{
              background-color: {self.selected_line_bg_color};
            }}
            {prefix} .text .highlight > pre > span.diff-add {{
              background-color: {self.diff_add_line_bg_color};
            }}
            {prefix} .text .highlight > pre > span.diff-add.selected {{
              background-color: {self.diff_add_selected_line_bg_color};
            }}
            {prefix} .text .highlight > pre > span.diff-remove {{
              background-color: {self.diff_delete_line_bg_color};
            }}
            {prefix} .text .highlight > pre > span.diff-remove.selected {{
              background-color: {self.diff_delete_selected_line_bg_color};
            }}'
        """
        return css
