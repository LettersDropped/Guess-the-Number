import  random   #importing the random module to create random numbers   


##Variables
ques = input("Do you want to start this game?\nReply with 'y' for yes and 'n' for no...\n")   #Asking questions to start the game
yans = "y"              #Users answer is Yes
nans = "n"              #Users answer is No
repn = "See you soon!"             #Printing No screen
guess = ''              #Empty variable to take the user's input

randnum = (random.randint(0,9))     #generating random numbers upto 9 with random module


##Main


#Taking the user input and printing the results


if ques == yans:                                            #Running the if statements to print the results
    guess = input("Guess the number betwenn 0 to 9: ")           
    if guess == randnum:
        print("You guessed the correct number!")
    else:
        print("Wrong Answer!, The correct answer is", randnum)
else:
    print(repn)         





