import pytest

def test_initial_check(conf_test_pytest_fixture):
    print("This is the first test case")

@pytest.mark.skip
def test_second_check():
    print("This is the second test case")