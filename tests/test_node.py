from lib.node import Node

def test_node_initializes_with_attributes():
    node = Node(13)

    actual_data = node.data
    actual_next = node.next

    expected_data = 13
    expected_next = None

    assert actual_data == expected_data
    assert actual_next == expected_next