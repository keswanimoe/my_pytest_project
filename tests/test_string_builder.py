from lib.string_builder import *

def test_string_builder_returns_name_string():
    string = StringBuilder()
    string.add("My name is Moesha")
    result = string.output()
    assert result == "My name is Moesha"

def test_string_builder_returns_name_string_size():
    string = StringBuilder()
    string.add("My name is Moesha")
    result = string.size()
    assert result == len("My name is Moesha")
    
def test_string_builder_returns_string():
    string = StringBuilder()
    string.add("Testing classes")
    result = string.output()
    assert result == "Testing classes"

def test_string_builder_returns_string_size():
    string = StringBuilder()
    string.add("Testing classes")
    result = string.size()
    assert result == len("Testing classes")