import json
import os
#import requests

url = "https://neal.fun/api/infinite-craft/pair"
default_elements = [{"🌬️ Wind": False}, {"🔥 Fire": False}, {"💧 Water": False}, {"🌍 Earth": False}]

def main():
    while len(input("First element:\t")) > 1:
        elements = []
        if os.path.exists("elements.json"):
            with open("elements.json", "r") as file:
                data = json.load(file)
                elements = data["elements"]
            missing_elements = [e for e in default_elements if e not in elements]
            if missing_elements:
                elements.extend(missing_elements)
                with open("elements.json", "w") as file:
                    json.dump({"elements": elements}, file)
            if not all(e.keys() for e in elements):
              with open("elements.json", "w") as file:
                json.dump({"elements": default_elements}, file)  
        else:
            create_elements()
                
def create_elements():
    with open("elements.json", "w") as file:
                json.dump({"elements": default_elements}, file)

if __name__ == "__main__":
    main()