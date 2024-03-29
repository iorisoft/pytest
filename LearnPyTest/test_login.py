import pytest

@pytest.mark.skip
def testLogin():
    print("Login Successful")


@pytest.mark.regression
def testLogoff():
    print("Logoff Successful")


@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4


@pytest.mark.xfail
def testCalculation1():
    assert 2 + 2 == 5