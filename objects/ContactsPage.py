from playwright.sync_api import Locator


class ContactsPage:
    def __init__(self,page):
        self.page = page
        self.office_phone_country_selector = self.page.locator("//select[@name='phone_country']")
        self.decision_maker_checkbox = self.page.get_by_role("checkbox", name="Decision maker")
        self.phone_number = self.page.locator("//input[@name='phone']")
