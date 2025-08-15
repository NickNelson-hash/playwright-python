from methods import CommonMethods, HomeMethods


def test_create_account(yetiforce_page):
    CommonMethods.yetiforce_login("demo","demo", yetiforce_page)
    HomeMethods.go_to_accounts_menu(yetiforce_page)