# File: tests/test_add_five.py

# This imports the function we want to test.
from lib.add_five import *

# Next, we create a single test example.
# The function name must start with `test_` for pytest to find it.
# The function should describe what the test verifies.
def test_add_five_returns_eight_for_three():
    # example argument
    result = add_five(3)
    
    # assert that ii this example it should return 8
    assert result == 8