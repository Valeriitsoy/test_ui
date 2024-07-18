from pages.base_page import BasePage
import allure


class ProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Opening a Greencart store page")
    def open(self) -> None:
        self.page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    @allure.step("Open product page")
    def click_on_product_card(self, product_name: str) -> None:
        self.page.locator(
            f'//h4[contains(text(), "{product_name}")]/preceding::img[@alt="{product_name} - 1 Kg"]'
        ).click()

    @allure.step("Product search in the search bar")
    def search_product(self, product_name: str) -> None:
        self.page.locator("//input[@type='search']").press_sequentially(product_name)
        self.page.wait_for_timeout(2000)

    @allure.step("Add a product to cart")
    def add_to_cart(self, product: str) -> None:
        self.page.locator(f'//h4[contains(text(), "{product}")]/following::button[1]').click()

    @allure.step('Open cart')
    def click_cart(self) -> None:
        self.page.locator('//a[@class="cart-icon"]/child::img').click()

    @allure.step("Click button - Proceed to checkout")
    def click_button_proceed_to_checkout(self) -> None:
        self.page.locator('//button[text()="PROCEED TO CHECKOUT"]').click()
