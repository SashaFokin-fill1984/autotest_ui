import pytest
from playwright.sync_api import expect
from pages.registration_page import RegistrationPage

@pytest.mark.parametrize("email,password,username", [
    ("user1@example.com", "pass1", "user1"),
    ("user2@example.com", "pass2", "user2"),
])
def test_successful_registration(registration_page: RegistrationPage,
                                 email: str, password: str, username: str):
    # открываем страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # заполняем форму
    registration_page.fill_registration_form(
        email=email, password=password, username=username
    )
    registration_page.click_registration_button()

    # переходим на дашборд и проверяем заголовок
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_title = registration_page.page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_have_text("Dashboard")