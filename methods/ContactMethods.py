
from playwright.sync_api import Page, expect

from methods.CommonMethods import CommonMethods
from objects.AccountPage import AccountPage
from objects.CommonObjects import CommonObjects
from objects.ContactsPage import ContactsPage


class ContactMethods:
    page:Page
    def __init__(self,yetiforce_page:Page):
        self.page = yetiforce_page

    def add_new_contact(self,data:dict):
        commonMethods = CommonMethods(self.page)
        commonObjects = CommonObjects(self.page)
        contactPage = ContactsPage(self.page)
        commonObjects.button("Add record").click()
        commonObjects.drop_down("Salutation").select_option(data["salutation"])
        commonMethods.enter_text_in_input_box("Last name",data["last_name"])
        toggle_panel = commonObjects.toggle_panel("Contact information")
        toggle_panel.scroll_into_view_if_needed()
        toggle_panel.click()
        contactPage.office_phone_country_selector.select_option(data["phone_country"])
        contactPage.phone_number.fill(data["phone_number"])
        commonObjects.toggle_panel("Custom information").click(force=True)
        commonObjects.input_box("Date of birth").fill(data["date_of_birth"])
        contactPage.decision_maker_checkbox.check()
        commonObjects.button("Save").click()
        expect(commonObjects.created_data_bread_crumb(data["last_name"])).to_be_visible()

