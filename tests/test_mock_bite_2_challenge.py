from unittest.mock import Mock

def test_creates_a_sophisticated_mock():
    # Uncomment and set up your mocks here
    task_list = Mock()
    task = Mock() 

    task_list.list.return_value = [task]
    task_list.count.return_value = 1
    task_list.clear.return_value = "success"

    # Don't edit below
    task_list.add(task)
    assert task_list.list() == [task]
    assert task_list.count() == 1
    assert task_list.clear() == "success"