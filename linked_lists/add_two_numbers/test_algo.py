import pytest
from .algo import add_two_numbers, ListNode

def test_serialize_list_node():
    node = ListNode(1, ListNode(2, ListNode(3)))
    assert node.as_list() == [1, 2, 3]

@pytest.mark.parametrize("l1, l2, expected", [
    ([1], [2], [3]),
    ([1, 1], [4, 2], [5, 3]),
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([1, 1], [2], [3, 1]),
])
def test_add_two_numbers(l1, l2, expected):
    result = add_two_numbers(ListNode.from_list(l1), ListNode.from_list(l2))
    assert result
    assert result.as_list() == expected

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
