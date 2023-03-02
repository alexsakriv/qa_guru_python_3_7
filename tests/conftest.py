import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser_with_size_1920_1080():
    browser.config.window_width = 1920
    browser.config.window_height = 1080