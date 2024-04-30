from lib.admin import validate_age
import pytest


def test_granted_access():
    assert validate_age('2008-04-25') == "Access granted"

def test_denied_access():
    assert validate_age('2008-04-26') == "Access denied. You are 15. You must be at least 16 years old."

def test_value():
    with pytest.raises(ValueError, match="Wrong format. Please use YYYY-MM-DD format"):
        validate_age('26-04-2008')

def test_type():
    with pytest.raises(TypeError, match="Wrong data type. Please enter a string using format YYYY-MM-DD"):
        validate_age(20080425)




