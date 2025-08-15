from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.username_field = page.get_by_placeholder('User')
        self.password_field = page.get_by_placeholder("Password")
        self.sign_in_button = page.get_by_role("button", name="Sign in")

