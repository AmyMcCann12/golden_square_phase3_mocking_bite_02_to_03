import pytest #type: ignore
from lib.diary import Diary
from lib.secret_diary import SecretDiary

"""
Given a diary, when a secret diary instance is created, diary cannot be read
"""
def test_secret_diary_initially_locked():
    diary = Diary("This is the contents of my diary")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

"""
Given a diary in secret diary, if the diary is unlocked, it can then be read
"""
def test_secret_diary_is_unlocked():
    diary = Diary("This is the contents of my diary")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "This is the contents of my diary"

"""
Given a diary in secret diary, 
if the diary is unlocked, then locked again, it can no longer be read.
"""

def test_secret_diary_is_unlocked_then_locked():
    diary = Diary("This is the contents of my diary")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read() 
    assert str(e.value) == "Go away!"