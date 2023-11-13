from lib.counter import *

def test_counter_returns_ten():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."
    
def test_counter_returns_three():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far."
    
def test_counter_returns_thirty():
    counter = Counter()
    counter.add(30)
    result = counter.report()
    assert result == "Counted to 30 so far."
    
def test_counter_returns_seventeen():
    counter = Counter()
    counter.add(17)
    result = counter.report()
    assert result == "Counted to 17 so far."