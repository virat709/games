import random

the_number = str(random.randint(10,99))
print("Guess the number. it contain two digits.")

remaining_tries = 7

while remaining_tries >0:
    player_guess = input("guess the number:")

    if player_guess == the_number:
        print("YES! you guessed it ")
        print("YOU WIN.")
        break
    else:
        bulls=0
        cows=0

        if player_guess[0]==the_number[0]:
            bulls +=1
        if player_guess[1]==the_number[1]:
            bulls +=1
        if player_guess [0]==the_number[1]:
            cows +=1
        if player_guess[1]==the_number[0]:
            cows +=1
        

        print("Bulls:",bulls)
        print("Cows: ",cows)

        remaining_tries -=1

        if remaining_tries<1:
            print("you lost the game.")
            break
