import pytest
from lib.present import *

def test_present_returns_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    
def test_present_returns_contents():
    present = Present()
    present.wrap("first test")
    result = present.unwrap()
    assert result == "first test"
    
def test_present_returns_contents_already_wrapped():
    present = Present()
    present.wrap("first test")
    with pytest.raises(Exception) as e:
        present.wrap("second test")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."