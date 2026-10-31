import pytest

@pytest.fixture(scope="function")
def prework():
    print("----This is the function instance----")

def test_seventh_check(prework):
    print("This is the seventh test case")

def test_eighth_check(conf_test_pytest_fixture):
    print("This is the eighth test case")