from playwright.sync_api import expect, Page

from objects.CommonObjects import CommonObjects
from objects.HomePage import HomePage
from objects.LoginPage import LoginPage

class CommonMethods:
    def __init__(self,yetiforce_page:Page):
        self.page = yetiforce_page

    def yetiforce_login(self,username: str, password: str):
        login = LoginPage(self.page)
        homepage = HomePage(self.page)
        login.username_field.fill(username)
        login.password_field.fill(password)
        login.sign_in_button.click()
        expect(homepage.companies_and_contacts_menu).to_be_visible()

    def select_option_from_dropdown(self,dropdown_name:str,dropdown_option:str):
        commonObjects = CommonObjects(self.page)
        commonObjects.drop_down("Legal form").click()
        commonObjects.drop_down_option(dropdown_option).click()

    def enter_text_in_input_box(self,name:str,value:str):
        commonObjects = CommonObjects(self.page)
        commonObjects.input_box(name).fill(value)




