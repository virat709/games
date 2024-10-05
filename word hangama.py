import random

def select_word():
    words= ["apple","orange","banana","pine apple","water menlon"]
    words= words [random.randint(0,len(words)-1)]
    return words

def blank_word():
    blankword = blank_word[0]
    for i in range (1,len(blank_word)):
        blankword += '_'
    return blankword

def word_hangman(word,so_far,letter,try_left):
    bad_try = True
    for i in range (0,len(word)):
        if word[i]== letter:
            so_far= so_far[:i]+letter+so_far[i+1]
            bad_try = False
        if bad_try is True:
            try_left -=1
            print('wrong try left:',try_left)
        print("so far you got:",so_far)
        if word == so_far:
            print("YAY!! You win")
        elif try_left ==0:
            print('Oops!!you lost')
        else:
            next_letter = input("enter the next letter:")
            word_hangman(word,so_far,next_letter,try_left)

word = select_word()
clue_word = blank_word(word)
word_hangman(word,clue_word,word[0],5)
