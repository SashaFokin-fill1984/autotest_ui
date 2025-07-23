from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator('//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    username_input = page.locator('//input[@id=":r1:"]')
    username_input.fill("user.name")

    password_input = page.locator('//input[@id=":r2:"]')
    password_input.fill("password")

    registration_button = page.locator('//button[@id="registration-page-registration-button"]')
    registration_button.click()

    valid_result = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(valid_result).to_have_text('Dashboard')

