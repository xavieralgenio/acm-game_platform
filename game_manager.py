import os
import importlib

GAMES_FILE = "data/games.txt"
GAMES_FOLDER = "games"


def load_games():
    """
    Reads games.txt and returns a list of game names.
    """

    if not os.path.exists(GAMES_FILE):
        return []

    with open(GAMES_FILE, "r") as f:
        games = [
            line.strip()
            for line in f.readlines()
            if line.strip()
        ]

    return games


def load_game_module(game_name):
    """
    Dynamically imports a game from /games folder.
    """

    try:
        module = importlib.import_module(f"{GAMES_FOLDER}.{game_name}")
        return module
    except ModuleNotFoundError:
        return None


def get_game_info(game_name):
    """
    Optional metadata from each game.
    """

    module = load_game_module(game_name)

    if module and hasattr(module, "get_info"):
        return module.get_info()

    return {
        "name": game_name.title(),
        "description": "No description available."
    }


def run_game(game_name):
    """
    Runs the game logic if available.
    """

    module = load_game_module(game_name)

    if module and hasattr(module, "run"):
        return module.run()

    return "Game could not be started."