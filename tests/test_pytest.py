def test_user():
    print("hello world")


class TestClass:
    def test_method(self):
        print("method")

    def test_method2(self):
        print("method2")


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, "2 + 2 should be 4"

def test_example():
    x = 5
    assert x == 6