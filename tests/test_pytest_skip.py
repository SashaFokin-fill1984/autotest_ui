import pytest

@pytest.mark.skip(reason="фича в разработке")
def test_feature_development():
    ...

@pytest.mark.skip(reason="фича в разработке")
class TestSuiteSkip:
    def test_feature_development_1(self):
        ...

    def test_feature_development_2(self):
        ...
