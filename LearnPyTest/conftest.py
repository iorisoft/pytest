import pytest


@pytest.fixture(autouse=True)
def setUp():
    print("Launch Browser")
    print("login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close Browser")