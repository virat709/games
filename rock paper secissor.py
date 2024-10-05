def winner (pl1,pl2):
    if pl1 ==pl2:
        return "Its tie!"
    elif pl1 == "rock":
        if pl2 == "secissor":
            return "first player win!"
        else:
            return "second player win!"
    elif pl1 == "paper":
        if pl2 == "rock":
            return "first player wins!"
        else:
            return "second player wins!"
    elif pl1 =="secisser":
        if pl2 == "paper":
            return "first player wins!"
        else:
            return "second player wins!"
    else:
        return "Invalid input!"
    
player1 = input("first player: rock, paper, secissor:")
player2 = input("second player: rock, paper, secissor:")

print(winner(player1,player2))
            