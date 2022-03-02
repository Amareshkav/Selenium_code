import pytest

@pytest.mark.signup
def test_four():
    assert 4 == 4

@pytest.mark.signin
def test_login():
    assert "A"+"M" == "AM"
