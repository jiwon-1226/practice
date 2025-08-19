import json
import os


def load_player():
    if os.path.exists("./save.json"):
        with open("./save.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return Player.from_dict(data)

def save_game(player):
    with open("./save.json", "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4, ensure_ascii=False)