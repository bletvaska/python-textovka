from helpers import get_item_by_name


def test_when_list_is_empty_then_return_none():
    assert get_item_by_name('name', []) is None, 'Item should be None.'
