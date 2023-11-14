from lib.gratitudes import *

def test_gratitudes_returns_test():
    gratitudes = Gratitudes()
    gratitudes.add("test")
    result = gratitudes.format()
    assert result == "Be grateful for: test"
    
def test_gratitudes_returns_my_health():
    gratitudes = Gratitudes()
    gratitudes.add("my health")
    result = gratitudes.format()
    assert result == "Be grateful for: my health"
    
def test_gratitudes_returns_my_family():
    gratitudes = Gratitudes()
    gratitudes.add("my brother")
    gratitudes.add("my sister")
    result = gratitudes.format()
    assert result == "Be grateful for: my brother, my sister"

