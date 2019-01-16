import random
import string
import re
from flask import Flask

wordlist = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]


word = random.choice(wordlist)
guess= []
original = list(word)
temp=list(word)
trial=0
counter = 0 
userinput = ""
lettersguessed = []

print("Welcome to play Hangman!!")
print("***************************")
for i in range(len(original)):
    if (original[i]) ==" ":
        guess.append(" ")
    else:
        guess.append("_")
guess1= " ".join(guess)
print("Word to be guessed: ", guess1)

length= (len(original)+3)

while length>trial:
    userinput=str.lower(input("Enter an alphabet: "))
    
    if not re.search("[A-Za-z]", userinput):
        print("This is not a letter", " ".join(guess))
        continue
    if userinput in lettersguessed:
        print("This letter already used once. ", " ".join(guess))
        continue
    else:
        lettersguessed.append(userinput)
    if len(userinput)>1:
        print("Enter only a single letter at a time")
        
    if userinput in original:
        while userinput in temp:
            counter= temp.index(userinput)
            guess[counter]= userinput
            temp.remove(userinput)
            temp.insert(counter, "_")
            
        counter=0
        for i in range(len(original)):
            if temp[i]=="_":
                counter+=1
        if counter == len(original):
            print("You have won")
            print("correct word\t", word)
            break
        print("Correct\t", " ".join(guess), "\ttrials left: ", (length-trial))
            
    else:
         trial+=1
         print("Incorrect\t", " ".join(guess), "\ttrials left: ",(length-trial))  
else:
    print("You lost!! Try again")  
    print("Correct answer was: ",word)   
    
    

