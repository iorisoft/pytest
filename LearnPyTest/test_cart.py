import pytest


@pytest.fixture
def setUp():
    print("Launch Browser")
    print("login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close Browser")

def testAddItemtoCart(setUp):
    print("Add Item Successful")


def testRemoveItemFromCart(setUp):
    print("Remove Item Successful")
