from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    login_button = page.get_by_test_id("registration-page-registration-button")
    expect(login_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.locator('//input[@id=":r1:"]')
    username_input.fill("user.name")

    password_input = page.locator('//input[@id=":r2:"]')
    password_input.fill("password")

    login_button = page.get_by_test_id("registration-page-registration-button")
    expect(login_button).to_be_enabled()

