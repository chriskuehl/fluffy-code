from fluffy_code import prebuilt_styles


def test_default_style():
    style = prebuilt_styles.default_style()
    assert style.name == "default"


def test_monokai_style():
    style = prebuilt_styles.monokai_style()
    assert style.name == "monokai"
