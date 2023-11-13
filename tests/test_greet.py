from lib.greet import *

def test_greet_returns_my_name():
    result = greet("Moesha")
    assert result == "Hello, Moesha!"