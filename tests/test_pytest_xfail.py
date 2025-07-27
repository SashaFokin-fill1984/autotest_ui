import pytest


@pytest.mark.xfail (reason="bug")
def test_with_bug():
    assert 1==2


@pytest.mark.xfail(reason="bug исправлен, маркировку не сняли")
def test_without_bug():
    ...
