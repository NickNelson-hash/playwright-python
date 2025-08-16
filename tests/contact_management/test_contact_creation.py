from playwright.sync_api import Page

from methods.AccountsMethod import AccountsMethod
from methods.CommonMethods import CommonMethods
from methods.ContactMethods import ContactMethods
from methods.HomeMethods import HomeMethods


def test_create_contact(yetiforce_page:Page):
    data = dict(
        last_name="Nickson Nelson",
        salutation="Mr.",
        phone_country="India",
        phone_number="7904416342",
        date_of_birth="1990-10-24"
    )

    commonMethods = CommonMethods(yetiforce_page)
    homeMethods = HomeMethods(yetiforce_page)
    contactsMethod = ContactMethods(yetiforce_page)
    commonMethods.yetiforce_login("demo","demo")
    homeMethods.go_to_contacts_menu()
    contactsMethod.add_new_contact(data)