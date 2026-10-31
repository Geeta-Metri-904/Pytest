import pytest

@pytest.fixture(scope = "module")
def prework():
    print("I setup module instance")
    return "fail"

@pytest.fixture(scope = "function")
def secondwork():
    print("I setup second work instance")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initialcheck(prework, secondwork):
    print("This is first test")
    assert prework == "fail"

@pytest.mark.skip
def test_secondcheck(prework, secondwork):
    print("This is second test")