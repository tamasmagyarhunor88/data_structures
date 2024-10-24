from lib.linked_list import LinkedList
from lib.node import Node

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