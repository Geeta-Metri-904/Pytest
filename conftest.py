import pytest

@pytest.fixture(scope="session")
def conf_test_pytest_fixture():
    print("----This is the conf test fixture browser instance----")