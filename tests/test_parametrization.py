import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_number(os: str, browser: str):
    assert len(os) + len(browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Test open {browser}')


@pytest.mark.parametrize('user', ['Alise', 'Zara'])
class TestOperations:

    @pytest.mark.parametrize('account', ['debt', 'credit'])
    def test_user_with_operation(self, user: str, account: str):
        print(f'User with operation: {user} ')

    def test_user_without_operation(self, user: str):
        print(f'User without operation: {user} ')


users = {
    "79999999999": 'User with mony on bank account',
    "79999999998": 'User without money on bank account',
    "79999999997": 'User wih operation on bank account'
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiars(phone_number: str):
    ...
