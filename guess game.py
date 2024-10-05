import random
print("To stop the game, enter: q")
score = 0

while True:
    num = random.randint(0,10)
    guess = input("guess the number between 0 to 10:")
    if guess== "q":
        print("Game over")
        break
    guess_num= int(guess)
    if guess_num ==num:
        print("Yes, you guessed it")
        print("YOU WIN")
        score += 10
        print("your new score:",score)
    else:
        print("not this number")
        print("the number was:",num)