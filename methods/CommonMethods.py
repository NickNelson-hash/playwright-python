from playwright.sync_api import expect

from objects.HomePage import HomePage
from objects.LoginPage import LoginPage

def yetiforce_login(username: str, password: str, yetiforce_page):
    login = LoginPage(yetiforce_page)
    homepage = HomePage(yetiforce_page)
    login.username_field.fill(username)
    login.password_field.fill(password)
    login.sign_in_button.click()
    expect(homepage.companies_and_contacts_menu).to_be_visible()



