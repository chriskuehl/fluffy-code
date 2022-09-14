import pytest

from fluffy_code import prebuilt_styles


@pytest.fixture
def default_style():
    return prebuilt_styles.default_style()
