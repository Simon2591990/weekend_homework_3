from app.models.player import Player

class Game():

    def rock_paper_scissors(player_1, player_2):
        if player_1.choice == "rock" and player_2.choice == "scissors":
            return player_1
    
        if player_1.choice == "scissors" and player_2.choice == "paper":
            return player_1
    
        if player_1.choice == "paper" and player_2.choice == "rock":
            return player_1
        
        if player_1.choice == player_2.choice:
            return None

        return player_2
