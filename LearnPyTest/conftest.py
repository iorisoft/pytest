import pytest


@pytest.fixture(autouse=False)
def setUp():
    print("Launch Browser")
    print("login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close Browser")