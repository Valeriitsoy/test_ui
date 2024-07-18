import allure
from playwright.sync_api import Page
from allure_commons.types import AttachmentType


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def report_screenshot(self, screenshot_name: str):
        allure.attach(
            body=self.page.screenshot(path=screenshot_name),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
