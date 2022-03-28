#Import Libraries

import random

#Define two arrays, weapons contains the 3 options the CPU can pick from, combos contains
#all possible combinations of attacker and defender choices
weapons = ["rock", "paper", "scissors"]
combos = ["rock-scissors", "paper-rock", "scissors-paper"]

#attacker (human) makes their choice and this is repeated back to them
attacker = input("Choose your weapon: ")
print("\nYou have chosen "+attacker)

#defender (cpu) makes their choice randomly form the weapons array and the human is told
#what the cpu chose
defender = random.choice(weapons)
print("\nThe computer has chosen "+defender)

#Function takes parameters of human choice, cpu choice, as well as all possible combinations array
def DecideWinner(attacker, defender, combos):
    
    #iterate through all possible combinations to find the right one
    for i in combos:

        #if human choice = cpu choice then it's a draw
        if attacker == defender:
            return "You drew :/"

        #if both human choice and cpu choice are in combination then we have the correct one.
        #combos array is ordered such that the word before the '-' in each item would be the winner
        #of the match up and thereofre we just need to return the characters before the '-' as the winner
        if attacker in i and defender in i:
            return (i.split('-')[0])
            

print("\n")

#simple logic to decide the winner based on the outcome of DecideWinner()
if attacker == DecideWinner(attacker,defender,combos):
    print("You win!")
elif defender == DecideWinner(attacker,defender,combos):
    print("You lose :(")
else:
    print(DecideWinner(attacker,defender,combos))