from flask import Flask, render_template
from game_manager import load_games

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/games")
def games():
    games = load_games()
    return render_template("games.html", games=games)


@app.route("/game/<name>")
def run_game(name):
    return render_template("game.html", game=name)


@app.route("/options")
def options():
    return render_template("options.html")


if __name__ == "__main__":
    app.run(debug=True)