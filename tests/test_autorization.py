from playwright.sync_api import expect, Page
import pytest
from pages.login_page import LoginPage

@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password"),
    ],
    ids=[
        "невалидный_email_и_password",
        "невалидный_email_и_пустой_password",
        "пустой_email_и_невалидный_password"
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.clic_login_button()
    login_page.check_visible_wrong_email_or_password_alert()



