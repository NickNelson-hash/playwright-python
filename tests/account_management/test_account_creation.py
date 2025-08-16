from playwright.sync_api import Page

from methods.AccountsMethod import AccountsMethod
from methods.CommonMethods import CommonMethods
from methods.HomeMethods import HomeMethods


def test_create_account(yetiforce_page:Page):
    data = dict(
        first_name="Nickson Nelson",
        short_name="Nickson12",
        legal_form="Private individual"
    )

    commonMethods = CommonMethods(yetiforce_page)
    homeMethods = HomeMethods(yetiforce_page)
    accountsMethod = AccountsMethod(yetiforce_page)
    commonMethods.yetiforce_login("demo","demo")
    homeMethods.go_to_accounts_menu()
    accountsMethod.add_new_account(data)