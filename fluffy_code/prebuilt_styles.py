import pygments.styles.monokai
import pygments.styles.xcode

from fluffy_code.style import StyleConfig


def default_style() -> StyleConfig:
    return StyleConfig.from_pygments_style(
        name='default',
        pygments_style=pygments.styles.xcode.XcodeStyle,
        ansi_fg_colors={
            'Black': '#000000',
            'Red': '#EF2929',
            'Green': '#62ca00',
            'Yellow': '#dac200',
            'Blue': '#3465A4',
            'Magenta': '#ce42be',
            'Cyan': '#34E2E2',
            'White': '#ffffff',
        },
        ansi_bg_colors={
            'Black': '#000000',
            'Red': '#EF2929',
            'Green': '#8AE234',
            'Yellow': '#FCE94F',
            'Blue': '#3465A4',
            'Magenta': '#c509c5',
            'Cyan': '#34E2E2',
            'White': '#ffffff',
        },
        border_color='#eeeeee',
        line_numbers_fg_color='#222222',
        line_numbers_bg_color='#fafafa',
        line_numbers_hover_bg_color='#ffeaaf',
        line_numbers_selected_bg_color='#ffe18e',
        selected_line_bg_color='#fff3d3',
        diff_add_line_bg_color='#e2ffe2',
        diff_add_selected_line_bg_color='#e8ffbc',
        diff_delete_line_bg_color='#ffe5e5',
        diff_delete_selected_line_bg_color='#ffdfbf',
    )


def monokai_style() -> StyleConfig:
    return StyleConfig.from_pygments_style(
        name='monokai',
        pygments_style=pygments.styles.monokai.MonokaiStyle,
        ansi_fg_colors={
            'Black': '#555753',
            'Red': '#FF5C5C',
            'Green': '#8AE234',
            'Yellow': '#FCE94F',
            'Blue': '#8FB6E1',
            'Magenta': '#FF80F1',
            'Cyan': '#34E2E2',
            'White': '#EEEEEC',
        },
        ansi_bg_colors={
            'Black': '#555753',
            'Red': '#F03D3D',
            'Green': '#6ABC1B',
            'Yellow': '#CEB917',
            'Blue': '#6392C6',
            'Magenta': '#FF80F1',
            'Cyan': '#2FC0C0',
            'White': '#BFBFBF',
        },
        border_color='#454545',
        line_numbers_fg_color='#999',
        line_numbers_bg_color='#272822',
        line_numbers_hover_bg_color='#8D8D8D',
        line_numbers_selected_bg_color='#5F5F5F',
        selected_line_bg_color='#545454',
        diff_add_line_bg_color='#3d523d',
        diff_add_selected_line_bg_color='#607b60',
        diff_delete_line_bg_color='#632727',
        diff_delete_selected_line_bg_color='#9e4848',
    )
