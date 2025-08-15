from objects.HomePage import HomePage


def go_to_accounts_menu(yetiforce_page):
    home_page = HomePage(yetiforce_page)
    home_page.companies_and_contacts_menu.click()
    home_page.left_navigation_menu("Accounts").click()