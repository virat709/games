import random

def get_clue():
    clues = ['_a_e','y_ll_w','o_a_g_','l__e','f_ee']
    position=random.randint(0,len(clues)-1)
    clue= clues[position]
    return clue

def check_match(the_clue,guess):
    if len(the_clue) != len(guess):
        return False
    for i in range (len(the_clue)):
        if the_clue[i] != '_' and the_clue [i] != guess[i]:
            return False
    return True

word = get_clue()
print('ypur word clue:',word)
answer = input('what would be the word:')

matched = check_match(word,answer)

if matched is True:
    print("WOW!!.You win.")
else:
    print("oops!!.you missed it.")
