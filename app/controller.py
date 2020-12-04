from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import Game

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
    player_1 = Player("Simon",player_1_choice)
    player_2 = Player("Laura", player_2_choice)
    winner =  Game.rock_paper_scissors(player_1, player_2)
    return render_template("results.html", winner = winner, player_1 = player_1, player_2 = player_2)


