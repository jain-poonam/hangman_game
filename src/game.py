"""Web service for Hangman Game and to expose different HTTP/REST api for clients 
to access web service.
"""
import random
import string
import re
from flask import Flask,render_template,request

app = Flask(__name__)

"List of words to be gueseed by the user"
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

"Starting Api route for the Welcome page of the Hangman Game"
@app.route('/')
def my_form():
    return render_template('form.html')

"To proceed the game further when Post request received and provide layout for the guess"
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

"To check the enter alphabets by the user and pops up message accordingly"
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
    return render_template('play.html',result = " ".join(guess))

if __name__ == "__main__":
    app.run()


 
    
    

