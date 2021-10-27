import  random   #importing the random module to create random numbers   


##Variables
ques = input("Do you want to start this game?\nReply with 'y' for yes and 'n' for no...\n")   #Asking questions to start the game
yans = "y"              #Users answer is Yes
nans = "n"              #Users answer is No
repn = "See you soon!"             #Printing No screen
guess = ''              #Empty variable to take the user's input

randnum = (random.randint(0,9))     #generating random numbers upto 9 with random module


#Taking the user input and printing the results running if-else statements to print the results..

if ques == yans:                         
    print("Okay, I am guessing the number between 0 to 9... Enter your number:")                                            #Running the if statements to print the results
    guess = int(input())           
    if guess == randnum:
        print("You guessed the correct number!")
    else:
        print(f"Wrong Answer!, The correct answer is {randnum} and your answer is {guess}")
else:
    print(repn)         





