from playwright.sync_api import sync_playwright, Page, expect
import pytest

@pytest.mark.registration
@pytest.mark.regression

def test_successful_registration(chromium_page: Page):
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user@gmail.com")

        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_have_text('Dashboard')

