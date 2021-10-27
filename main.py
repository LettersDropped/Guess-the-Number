import  random   #importing the random module to create random numbers   


##Variables
ques = input("Do you want to start this game?\nReply with 'y' for yes and 'n' for no\n")   #Asking questions to start the game
yans = "y"              #Users answer is Yes
repn = ":("             #Users answer is No
guess = ''              #Empty variable to take the user's input

randnum = (random.randint(0,9))     #generating random numbers upto 9 with random module


##Main


#Taking input from the User to start the game


if ques == yans:
    guess = input("Guess the number betwenn 0 to 9: ")
else:
    print(repn)                    


#Printing the results


if guess == randnum:
    print("You guessed the correct number!")
else:
    print("Wrong Answer!, The correct answer is", randnum)


