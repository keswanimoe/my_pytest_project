from lib.report_length import * 

def test_report_length_returns_four():
    result = report_length("test")
    assert result == "This string was 4 characters long."
    
def test_report_length_returns_five():
    result = report_length("test ")
    assert result == "This string was 5 characters long."
    
def test_report_length_returns_seven():
    result = report_length("testing")
    assert result == "This string was 7 characters long."
    
def test_report_length_returns_twelve():
    result = report_length("test testing")
    assert result == "This string was 12 characters long."