import  random     

ques = input("Do you want to start this game?\nReply with 'y' for yes and 'n' for no...\n")   
yans = "y"              
nans = "n"              
repn = "See you soon!"             
guess = ''              

randnum = (random.randint(0,9))     

if ques == yans:                         
    print("Okay, I am guessing the number between 0 to 9... Enter your number:")                                            #Running the if statements to print the results
    guess = int(input())           
    if guess == randnum:
        print("You guessed the correct number!")
    else:
        print(f"Wrong Answer!, The correct answer is {randnum} and your answer is {guess}")
else:
    print(repn)         





