import allure
import pytest
from pages.product_page import ProductPage
from playwright.sync_api import expect


@allure.epic("Product Page Functionality")
class TestProductPage:

    @allure.feature("Product page opening")
    @pytest.mark.smoke
    def test_open_product(self, page):
        product_page = ProductPage(page)
        product_page.open()
        product_page.click_on_product_card('Tomato')
        locator = page.locator('//div[@class="quick-view-image"]/child::img')
        product_page.report_screenshot('shop.png')
        expect(locator, "Product page opening error").to_be_visible()

    @allure.feature("Search product")
    @pytest.mark.smoke
    def test_search_product(self, page):
        product_page = ProductPage(page)
        product_page.open()
        product_page.search_product('Potato')
        locator = page.locator('//div[@class="product"]//following::h4')
        expect(locator, "Product search error").to_contain_text("Potato")

    @allure.feature("Adding a product to the cart and proceeding to payment")
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_product_payment(self, page):
        product_page = ProductPage(page)
        product_page.open()
        product_page.add_to_cart('Cucumber')
        product_page.click_cart()
        product_page.click_button_proceed_to_checkout()
        locator = page.locator('//button[text()="Place Order"]')
        expect(locator, "Adding a product to the cart and proceeding to payment error").to_be_visible()

    @allure.feature("Adding a product to the cart")
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_add_product_to_cart(self, page):
        product_page = ProductPage(page)
        product_page.open()
        product_page.add_to_cart('Brocolli')
        product_page.click_cart()
        locator = page.locator('//ul[@class="cart-items"]/following::p[@class="product-name"]')
        expect(locator, "Adding a product to the cart error").to_contain_text("Brocolli")

    @allure.feature("Invalid product search")
    @pytest.mark.regress
    def test_search_invalid_product(self, page):
        product_page = ProductPage(page)
        product_page.open()
        product_page.search_product('InvalidValue')
        expect(page.get_by_text('Sorry, no products matched your search!')).to_be_visible()

