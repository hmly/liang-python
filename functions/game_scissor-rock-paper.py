from random import randint

def gameScissorRockPaper():
    choices = ['Scissor', 'Rock', 'Paper']
    user = eval(input("Enter a (0)Scissor, (1)Rock, (2)Paper: "))
    comp = randint(0,2)

    print ("User's choice:", choices[user], "\nComp's choice:", choices[comp])
    
    if (user > comp and user != 0):
        print ("The user win!")
    elif (user == 0 and comp == 2):
        print ("The user win!")
    elif (user == 2 and comp == 0):
        print ("The comp win!")
    elif (user == comp):
        print ("It's a tie!")
    else:
        print ("The comp win!")

# Test Run
print (gameScissorRockPaper())
