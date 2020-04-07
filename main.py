##################################################################
# Interactive English Dictionary
# Description:
# This program takes a string and outputs the definition
# of the string from a database file of definitions
##################################################################

# Module import
# - json to import json
# difflib to compare strings

import json
from difflib import get_close_matches
data = json.load(open("data.json","r"))
userWord = ""

# Function
# function for returning definition of word
def getDefn(word):
    # exit word
    if(word == "\end"):
        return word
    #else print the word in the data set
    else:
        # Check for "standard" words
        if word in data:
            return data[word]
        # Check for proper nouns
        elif word.title() in data:
            return data[word.title()]
        # Check for items such as acronyms (FBI, WHO)
        elif word.upper() in data:
            return data[word.upper()]
        # if word doesn't exist, print first close match
        elif len(get_close_matches(word, data.keys())) > 0:
            yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead?  Enter Y if yes, or N if no:  ")
            # if user likes match, then use this as parameter to return definition
            if(yn.lower() == "y"):
                return data[get_close_matches(word, data.keys())[0]]
            # if user doesn't like suggestion, word does not exist
            elif(yn.lower() == "n"):
                return("The word cannot be found in the dictionary")
            # if neither 'y' or 'n' are entered, input is invalid
            else:
                while (yn != "y" and yn != "n"):
                    print("Answer must either be 'y' or 'n'")
                    yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead?  Enter Y if yes, or N if no:  ")
                    
        # word cannot be found, and no close matches
        else:
            return("That word cannot be found in the dictionary")

# Main
# exit word for loop, asking user input
while(userWord != "\end"):
    userWord = input("Input a word to define, '\end' to exit : ").lower()
    if(userWord == "\end"):
        break
    else:
        # if ouput is list, increment and output sequentially
        output = getDefn(userWord)
        if(isinstance(output, list)):
            for defn in output:
                print(f"\n{defn}")
        # if not, output standard string
        else:
            print(f"\n{output}")