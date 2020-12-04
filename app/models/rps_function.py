def rock_paper_scissors(player_1, player_2):
    if player_1.choice == "rock" and player_2.choice == "scissors":
        return "Player 1 wins with rock!"
    
    if player_1.choice == "scissors" and player_2.choice == "paper":
        return "Player 1 wins with scissors!"
    
    if player_1.choice == "paper" and player_2.choice == "rock":
        return "Player 1 wins with paper!"

    return f"Player 2 wins with {player_2.choice}!"

