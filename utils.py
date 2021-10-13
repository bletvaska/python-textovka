def get_item_by_name(name: str, items: list) -> dict:
    for item in items:
        if item['name'] == name:
            return item

    # return None