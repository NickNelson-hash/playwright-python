

from playwright.sync_api import Page, Locator


class HomePage:
    page:Page = None
    def __init__(self, page:Page):
        self.companies_and_contacts_menu = page.locator("//span[@class='c-menu__item__icon yfm-CompaniesAndContact']")
        self.page = page

    def left_navigation_menu(self,name:str)->Locator:
        return self.page.locator("//span[contains(@class,'menu__item') and @title='"+name+"']")