import random
import string
import re
from flask import Flask,render_template,request

app = Flask(__name__)

wordlist = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]


word = ""
guess= []
original = []
temp=[]
trial=0
counter = 0 
lettersguessed = []
length=0


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    global guess
    global word
    global original
    global temp
    global trial
    global counter
    global lettersguessed
    global length
    
    guess.clear()
    trial = 0
    counter = 0
    length = 0
    lettersguessed.clear()
    word = random.choice(wordlist)
    original = list(word)
    temp=list(word)

    text = request.form['text']
    processed_text = text.upper()
    if processed_text=="NO":
        return render_template('form.html')
    else:
        for i in range(len(original)):
            if (original[i]) ==" ":
                guess.append(" ")
            else:
                guess.append("_")
        guess1= " ".join(guess)
        length= (len(original)+3)
        return render_template('play.html',result = guess1)
#         return("Word to be guessed: "+ guess1)

@app.route('/play', methods=['POST'])
def my_play_post():
    text = request.form['text']
    userinput = text.lower()
    global trial
    if (length > trial):
        trial+=1
        if not re.search("[A-Za-z]", userinput):
            return render_template('play.html',result = " ".join(guess),error="Not an Alphabet")
        if len(userinput)>1:
            return render_template('play.html',result = " ".join(guess),error="Only one alphabet is allowed!")
        if userinput in lettersguessed:
            return render_template('play.html',result = " ".join(guess),error="Already guessed alphabet")
        else:
            lettersguessed.append(userinput)
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
                return render_template('won.html',result = word)
        else:
            return render_template('play.html',result = " ".join(guess),error="Incorrect Alphabet")
    else:
        return render_template('form.html',result ="You have lost!! Correct word is: "+ word)   
#         
    return render_template('play.html',result = " ".join(guess))

if __name__ == "__main__":
    app.run()


# length= (len(original)+3)
#  
# while length>trial:
#     userinput=str.lower(input("Enter an alphabet: "))
#      
#     if not re.search("[A-Za-z]", userinput):
#         print("This is not a letter", " ".join(guess))
#         continue
#     if userinput in lettersguessed:
#         print("This letter already used once. ", " ".join(guess))
#         continue
#     else:
#         lettersguessed.append(userinput)
#     if len(userinput)>1:
#         print("Enter only a single letter at a time")
#          
#     if userinput in original:
#         while userinput in temp:
#             counter= temp.index(userinput)
#             guess[counter]= userinput
#             temp.remove(userinput)
#             temp.insert(counter, "_")
#              
#         counter=0
#         for i in range(len(original)):
#             if temp[i]=="_":
#                 counter+=1
#         if counter == len(original):
#             print("You have won")
#             print("correct word\t", word)
#             break
#         print("Correct\t", " ".join(guess), "\ttrials left: ", (length-trial))
#              
#     else:
#          trial+=1
#          print("Incorrect\t", " ".join(guess), "\ttrials left: ",(length-trial))  
# else:
#     print("You lost!! Try again")  
#     print("Correct answer was: ",word)   
    
    

