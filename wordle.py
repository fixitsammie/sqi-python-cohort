import random
from tabulate import tabulate
import sys

from termcolor import colored, cprint
attempts=6
guess_list = ["enact","price","beast","verse","crown"]
guess_word = random.choice(guess_list)



def gen_color(text):
    word_=[]
    for i,char in enumerate(text):
        if char in guess_word and text[i]==guess_word[i]:
            word_.append(colored(char.upper(),"green"))
        elif char in guess_word:
            word_.append(colored(char.upper(),"yellow"))
        else:
            word_.append(char.upper())
    return word_

table = [[colored("0", "red",attrs=["concealed"])]*5 for i in range(5)]
#table[0][0] = colored("H", "red")
start_game_table = [[colored("0", "red",attrs=["concealed"])]*5 for i in range(5)]
wordle_ = [colored(char.upper(),"green") for char in list("wrdle")]
start_game_table[2]=wordle_

print("Welcome to the game")
cprint((tabulate(start_game_table, tablefmt="simple_grid")))
print("\n")
game_round=1

while game_round<=5:
    round_guess=input("Guess a 5 letter word\n")
    while len(round_guess)!=5:
        round_guess=input("Guess a 5 letter word\n")
    table[game_round-1]=gen_color(round_guess)
    cprint(tabulate(table, tablefmt="simple_grid"))
    
    if round_guess == guess_word:
        print("You guessed the word correctly. You win!")
        break
    if game_round == 5:
        print("Gameover")
    game_round+=1

    



    