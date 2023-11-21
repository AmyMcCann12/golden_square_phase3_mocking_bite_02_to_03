from lib.diary import Diary

"""
When a diary is created, check that the given contents 
is assigned to the contents property
"""

def test_diary_created_contents_assigned():
    diary = Diary("This is my diary")
    assert diary.contents == "This is my diary"

"""
When a diary is read, the contents of the diary is returned
"""

def test_diary_read_returns_contents():
    diary = Diary("This is my diary contents")
    assert diary.read() == "This is my diary contents"