import pytest

@pytest.fixture

def clear_books_database():
    print("[Fixture] Clearing books database")


@pytest.fixture
def fill_books_database():
    print("[Fixture] Filling books database")


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Reading all books")

@pytest.mark.usefixtures(
'clear_books_database',
'fill_books_database'
)
class TestLibrary:
    def test_read_all_books_in_library(self):
        ...

    def test_delete_book(self):
        ...