import requests

API_URL = "https://minecraft-ids.grahamedgecombe.com/items.json"

def get_items():
    response = requests.get(API_URL)

    if response.status_code != 200:
        print("Error fetching API:", response.status_code)
        print(response.text)
        return None

    return response.json()

def get_tool(tool_name):
    items = get_items()

    if items is None:
        return None

    for item_id in items:
        if tool_name.lower() in item_id.lower():
            return item_id

    return None