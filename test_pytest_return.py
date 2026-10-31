import pytest

@pytest.fixture(scope="module")
def prework():
    print("----This is the module instance----")
    return "pass"

def test_fifth_check(prework):
    print("This is the fifth test case")
    assert prework == "pass"

@pytest.mark.smoke
def test_sixth_check(conf_test_pytest_fixture):
    print("This is the sixth test case")