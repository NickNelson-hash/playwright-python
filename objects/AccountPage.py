from playwright.sync_api import Locator


class AccountPage:
    def __init__(self,page):
        self.page = page

    def created_account_bread_crumb(self,first_name:str)->Locator:
        return self.page.locator("//li[contains(@class,'breadcrumb') and text()='"+first_name+"']'")