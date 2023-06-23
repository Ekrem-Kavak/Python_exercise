# Ask the user to create a password. This password must have least 8 characters, 1 lowercase letter and 1 uppercase letter. It must also contain at least one of the characters specified in the character list. 

import re

character = ["\?","\*","\!","\%"]

def passwordCheck(password):
    if len(password)<= 8:
        raise Exception("Your password must be at least 8 character!")
    elif not re.search("[a-z]",password):
        raise Exception("Your password must contain at least one lowercase letter.") 
    elif not re.search("[A-Z]", password):
        raise Exception("Your password must contain at least one uppercase letter.")
    elif not re.search("[0-9]",password):
        raise Exception("Your password must contain at least one number")
    elif not re.search(str(character),password):
        raise Exception("Your password must contain at least one ('?','*','!','%') characters.")
    else:
        print("Your password has been successfully created.")

while True:
    try:
        password = input("Please, created your password: ")
        passwordCheck(password)
    except Exception as exp:
        print(exp)
    else:
        break


    

