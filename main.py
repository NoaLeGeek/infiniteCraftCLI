import json
import os
import requests

url = "https://neal.fun/api/infinite-craft/pair"
default_elements = [{"🌬️ Wind": False}, {"🔥 Fire": False}, {"💧 Water": False}, {"🌍 Earth": False}]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Referer": "https://neal.fun/infinite-craft/",
    "Alt-Used": "neal.fun",
}

def main():
    elements = []
    if not os.path.exists("elements.json"):
        create_elements()
    with open("elements.json", "r") as file:
        data = json.load(file)
        elements = data["elements"]
    missing_elements = [e for e in default_elements if e not in elements]
    if missing_elements:
        elements.extend(missing_elements)
        with open("elements.json", "w") as file:
            json.dump({"elements": elements}, file)
    ask_elements()
    
        
def ask_elements():
    first = input("First element:\t")
    second = input("Second element:\t")
    if len(first) > 1 and len(second) > 1:
        combine_elements(first, second)


def combine_elements(first, second):
    response = requests.get(url, headers=headers, params={"first": first, "second": second})
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, "Error!")


def create_elements():
    with open("elements.json", "w") as file:
                json.dump({"elements": default_elements}, file)


if __name__ == "__main__":
    main()