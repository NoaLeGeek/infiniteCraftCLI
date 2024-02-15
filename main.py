import json
import os
import requests

url = "https://neal.fun/api/infinite-craft/pair"
elements = {}
recipes = {}
default_elements = {"🌬️ Wind": False, "🔥 Fire": False, "💧 Water": False, "🌍 Earth": False}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Referer": "https://neal.fun/infinite-craft/",
    "Alt-Used": "neal.fun",
}

def main():
    global elements
    if not os.path.exists("elements.json"):
        create_elements()
    if not os.path.exists("recipes.json"):
        with open("recipes.json", "w") as file:
            json.dump({"recipes", {}}, file)
    with open("elements.json", "r") as file:
        data = json.load(file)
        elements = data["elements"]
    print(elements)
    with open("recipes.json", "r") as file:
        data = json.load(file)
        recipes = data["recipes"]
    missing_elements = {default_element: False for default_element in default_elements if default_element not in list(elements.keys())}
    print(missing_elements)
    if missing_elements:
        elements.update(missing_elements)
        with open("elements.json", "w") as file:
            json.dump({"elements": elements}, file)
    ask_elements()
    
        
def ask_elements():

    first = input("First element:\t")
    if len(first) < 2:
        return
    if first not in [e.split(" ")[1] for e in list(elements.keys())]:
        print(f"You don't have {first} yet! Try again with a different element.")
        ask_elements()
        return
    second = input("Second element:\t")
    if len(second) < 2:
        return
    if second not in [e.split(" ")[1] for e in list(elements.keys())]:
        print(f"You don't have {second} yet! Try again with a different element.")
        ask_elements()
        return
    combine_elements(first, second)


def add_element(name, emoji, isNew):
    elements[f"{emoji} {name}"] = isNew
    with open("elements.json", "w") as file:
        json.dump({"elements": elements}, file)
    print(f"Discovered {emoji} {name}!")
    ask_elements()


def combine_elements(first, second):
    response = requests.get(url, headers=headers, params={"first": first, "second": second})
    if response.status_code == 200:
        new_element = response.json()
        if new_element["result"] == "Nothing":
            print("Nothing happened.")
        save_recipe(first, second, new_element["result"], new_element["emoji"])
        add_element(new_element["result"], new_element["emoji"], new_element["isNew"])
    else:
        print(response.status_code, "Error!")


def save_recipe(first, second, element, emoji):
    element = f"{emoji} {element}"
    if emoji + " " + element not in list(recipes.keys()):
        recipes[element] = []
    if [first, second] in recipes[element] or [second, first] in recipes[element]:
        return
    recipes[element].append([first, second])
    with open("recipes.json", "w") as file:
        json.dump({"recipes": recipes}, file)



def create_elements():
    with open("elements.json", "w") as file:
                json.dump({"elements": default_elements}, file)


if __name__ == "__main__":
    main()