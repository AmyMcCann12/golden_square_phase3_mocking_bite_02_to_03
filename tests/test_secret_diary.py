from lib.secret_diary import SecretDiary
from unittest.mock import Mock
import pytest #type: ignore

"""
When a secret diary is created, the diary is initially locked and the 
contents cannot be read
"""

def test_secret_diary_cannot_be_read_initially():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    with pytest.raises(Exception) as e:
        secret_diary.read() 
    assert str(e.value) == "Go away!"
    fake_diary.read.assert_not_called()

"""
When a secret diary is created, and then unlocked, 
the contents will be returned when the read method is called.
"""

def test_secret_diary_contents_unlocked():
    fake_diary = Mock()
    fake_diary.read.return_value = "This is the contents of my diary"
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == "This is the contents of my diary"
    fake_diary.read.assert_called()

"""
When a secret diary is created, unlocked and then locked,
the contents can no longer be read
"""

def test_secret_diary_contents_locked():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read() 
    assert str(e.value) == "Go away!"
    fake_diary.read.assert_not_called()
