
from playwright.sync_api import Page, expect

from methods.CommonMethods import CommonMethods
from objects.AccountPage import AccountPage
from objects.CommonObjects import CommonObjects




class AccountsMethod:
    page:Page
    def __init__(self,yetiforce_page:Page):
        self.page = yetiforce_page

    def add_new_account(self,data:dict):
        commonMethods = CommonMethods(self.page)
        commonObjects = CommonObjects(self.page)
        accountPage = AccountPage(self.page)
        commonObjects.button("Add record").click()
        commonObjects.drop_down("Legal form").select_option(data["legal_form"])
        commonMethods.enter_text_in_input_box("Account name",data["first_name"])
        commonMethods.enter_text_in_input_box("Short name",data["short_name"])
        commonObjects.button("Save").click()
        expect(accountPage.created_account_bread_crumb(data["first_name"])).to_be_visible()

