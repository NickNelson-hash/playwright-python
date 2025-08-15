from objects.LoginPage import LoginPage

def yetiforce_login(username: str, password: str, login_page):
    login = LoginPage(login_page)
    login.username_field.fill(username)
    login.password_field.fill(password)
    login.sign_in_button.click()


