import pytest

@pytest.fixture()
def prework():
    print("----This is the browser instance----")

def test_third_check(prework):
    print("This is the third test case")

def test_fourth_check(conf_test_pytest_fixture):
    print("This is the fourth test case")