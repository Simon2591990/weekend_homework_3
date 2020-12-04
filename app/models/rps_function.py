def rock_paper_scissors(player_1, player_2):
    if player_1 == "rock" and player_2 == "scissors":
        return "Player 1 wins with rock!"
    
    if player_1 == "scissors" and player_2 == "paper":
        return "Player 1 wins with scissors!"
    
    if player_1 == "paper" and player_2 == "rock":
        return "Player 1 wins with paper!"

    return f"Player 2 wins with {player_2}!"

