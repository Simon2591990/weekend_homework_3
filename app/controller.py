from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import Game
import random

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/<player_1_choice>/<player_2_choice>")
# def rps(player_1_choice, player_2_choice):
#     player_1 = Player("Simon",player_1_choice)
#     player_2 = Player("Laura", player_2_choice)
#     winner =  Game.rock_paper_scissors(player_1, player_2)
#     if winner != None:
#         return f"{winner.name} wins with {winner.choice}!"
#     else:
#         return "It's a draw!"

@app.route("/<player_1_choice>/<player_2_choice>")
def rps_results(player_1_choice, player_2_choice):
    player_1 = Player("Player 1",player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    winner =  Game.rock_paper_scissors(player_1, player_2)
    return render_template("results.html", winner = winner, player_1 = player_1, player_2 = player_2)

@app.route("/play", methods=["GET"])
def play():
    # computer = Player("Computer", "rock")
    # player_name = request.form["player_name"]
    # player_choice = request.form["player_choice"]
    # player = Player(player_name, player_choice)
    # winner = Game(computer, player)
    return render_template("play.html")

@app.route("/play_results", methods=["POST"])
def play_computer():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer = Player("Computer", computer_choice)
    name = request.form["player_name"]
    choice = request.form["player_choice"]
    player = Player(name, choice)
    winner = Game.rock_paper_scissors(computer, player)
    return (render_template("play_results.html", computer = computer, player = player, winner = winner))




