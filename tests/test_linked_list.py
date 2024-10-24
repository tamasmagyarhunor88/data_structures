from lib.linked_list import LinkedList
from lib.node import Node
import pytest

def test_linked_list_instantiates_with_attribute():
    linked_list = LinkedList()

    actual = linked_list.head
    expected = None

    assert actual == expected

def test_linked_list_appends_to_head_if_head_is_none():
    linked_list = LinkedList()
    linked_list.append(13)

    actual = linked_list.head.data
    expected = 13

    assert actual == expected

def test_linked_list_appends_to_end_if_head_exists():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(16)
    linked_list.append(20)

    actual = linked_list.head.next.next.data
    expected = 20

    assert actual == expected

def test_linked_list_insert_to_index_zero():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(16)
    linked_list.append(20)
    linked_list.insert(0, 5)

    actual = linked_list.head.data
    expected = 5

    assert actual == expected

def test_linked_list_insert_to_any_index():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(16)
    linked_list.append(20)
    linked_list.insert(2, 5)

    actual = linked_list.head.next.next.data
    expected = 5

    assert actual == expected

def test_linked_list_insert_to_end():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(16)
    linked_list.append(20)
    linked_list.insert(3, 5)

    actual = linked_list.head.next.next.next.data
    expected = 5

    assert actual == expected

def test_linked_list_insert_to_any_index():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(16)
    linked_list.append(20)
    linked_list.insert(2, 5)

    actual = linked_list.head.next.next.data
    expected = 5

    assert actual == expected

def test_linked_list_length_method():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(16)
    linked_list.append(20)

    actual = linked_list.length()
    expected = 3

    assert actual == expected

def test_linked_list_insert_raises_error_if_range_lower_than_zero():
    linked_list = LinkedList()
    linked_list.append(13)

    with pytest.raises(IndexError) as e:
        linked_list.insert(-2, 5)

    actual = str(e.value)
    expected = "Index out of range"

    assert actual == expected  

def test_linked_list_insert_raises_error_if_range_bigger_than_length():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(3)

    with pytest.raises(IndexError) as e:
        linked_list.insert(5, 8)

    actual = str(e.value)
    expected = "Index out of range"

    assert actual == expected

def test_linked_list_searched_for_data():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(3)
    linked_list.append(5)

    actual = linked_list.search(13)
    expected = True

    assert actual == expected

def test_linked_list_searched_for_data():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(3)
    linked_list.append(5)

    actual = linked_list.search(23)
    expected = False

    assert actual == expected

def test_linked_list_repr():
    linked_list = LinkedList()
    linked_list.append(13)
    linked_list.append(3)
    linked_list.append(5)

    actual = str(linked_list)
    expected = "13 => 3 => 5"

    assert actual == expected