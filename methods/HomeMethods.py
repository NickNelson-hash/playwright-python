import time

from playwright.sync_api import Page

from objects.HomePage import HomePage

class HomeMethods:
    def __init__(self,yetiforce_page:Page):
        self.page = yetiforce_page

    def go_to_accounts_menu(self):
        home_page = HomePage(self.page)
        home_page.companies_and_contacts_menu.hover()
        time.sleep(2)
        home_page.expanded_left_navigation_menu("Companies and Contacts").click()
        home_page.left_navigation_menu("Accounts").click()

    def go_to_contacts_menu(self):
        home_page = HomePage(self.page)
        home_page.companies_and_contacts_menu.hover()
        time.sleep(2)
        home_page.expanded_left_navigation_menu("Companies and Contacts").click()
        home_page.left_navigation_menu("Contacts").click()