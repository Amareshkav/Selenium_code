import pytest

@pytest.mark.signin
def test_one():
    assert 1 == "1"


def test_login():
    assert "amaresh".capitalize() == "Amaesh"


def test_three():
    assert 1*4 == 4

