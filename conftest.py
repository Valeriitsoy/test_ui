import pytest
from playwright.sync_api import sync_playwright
from pages.product_page import ProductPage


@pytest.fixture(scope='session')
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()


@pytest.fixture
def product_page(browser_context):
    page = browser_context.new_page()
    product_page = ProductPage(page)
    product_page.open()
    yield product_page
    page.close()
