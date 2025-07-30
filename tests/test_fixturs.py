import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOTEST] Sending analytics data...")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Loading settings...",)
@pytest.fixture(scope="class")
def user():
    print("[CLASS] Creating user...")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Starting browser...")


class TestUserFlow:
    def test_user_can_login(self, user, browser, settings):
        ...
    def test_user_can_logout(self, user, browser, settings):
        ...


class TestAccountFlow:
    def test_user_account(self, user, browser, settings):
        ...
