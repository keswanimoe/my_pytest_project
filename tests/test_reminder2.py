import pytest
from lib.reminder2 import Reminder2

def test_reminder2():
    reminder = Reminder2("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"