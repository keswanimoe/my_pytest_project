import pytest
from lib.password_checker import *

def test_password_checker_returns_true():
    password_checker = PasswordChecker()
    result = password_checker.check("aaaaaaaa")
    assert result == True 

def test_password_checker_returns_invalid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("aaaaaa")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters." 