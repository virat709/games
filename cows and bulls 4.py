import random

secret_number = str(random.randint(1000,9999))
print("Guess the number. Number contain 4 digits.")

remaining_try = 10

def my_bulls_cows(num,user):
    cowsandbulls = [0,0]
    for i in range (len(num)):
        if user[i] == num[1]:
            cowsandbulls [0] +=1
        elif user [i] in num:
            cowsandbulls[1] +=1
    
    
    return cowsandbulls

while remaining_try >0:
    player_guess = input("enter the guess:")

    if player_guess == secret_number:
        print("Yes, you guessed it.")
        print("YOU WIN")
        break
    else:
        cows_bulls = my_bulls_cows(secret_number,player_guess)
        print("Bulls",cows_bulls[0])
        print("Cows",cows_bulls[1])

        remaining_try < 1

        if remaining_try <1:
            print("You lost the game.")
            break
     
