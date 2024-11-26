import random
i = 0
playerScore = 0
compScore = 0

while i < 5 :
    choices = ["rock", "paper", "scissor"]
    player = input ("Your move: ").lower()
    comp = random.choice(choices)
    print (f"computer's move: {comp}")
    i += 1

    if player == "rock" :
        if comp == "scissors" :
            print ("You win the round")
            playerScore += 1

        elif comp == "paper" :
            print ("You loose the round")
            compScore += 1

        else :
            print ("Tie")
    
    elif player == "paper" :
        if comp == "rock" :
            print ("You win the round")
            playerScore += 1

        elif comp == "scissor" :
            print ("You loose the round")
            compScore += 1

        else :
            print ("Tie")

    elif player == "scissor" :
        if comp == "paper" :
            print ("You win the round")
            playerScore += 1

        elif comp == "rock" :
            print ("You loose the round")
            compScore += 1

        else :
            print ("Tie")


if playerScore > compScore :
    print ("Congratulations!! You won the game")
elif playerScore < compScore :
    print ("Oops!! You lost the game")
else :
    print ("The game has tied")
            
print (f"Computer has won {compScore} times")
print (f"You have won {playerScore} times")