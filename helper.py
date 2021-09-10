def find_item(name: str, items: list):
    for item in items:
        if item['name'] == name:
            return item

    return None
