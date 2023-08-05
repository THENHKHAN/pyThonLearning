'''
Status ==> Completed
'''

# Some references are attached at the bottom

import random

player_name = input("\n\n \t Hello, What's your name?  ")
print('\t\t Hey! '+ player_name + '\n\t So You have 5 Chances to guess the number between 1 to 100:\n')

compNum = random.randint(1,101) # random number generated
chance = 0
while (True) :
    if (chance < 5) :
            userNum = int(input(f"please enter your {chance+1} Guess: "))
            print(f"Random number Genereted by Computer: {compNum}")

            if (userNum > compNum or userNum < compNum ) :
                if userNum > compNum and abs(userNum-compNum) > 10 :
                       print(f"you are too HIGH!!!")
               
                elif userNum < compNum and abs(userNum-compNum) > 10 :
                        print(f"you are too LOW!!!")
                
                else :
                    print(f"you were too close to win!!!")

            elif (compNum == userNum):
                    print(f"YOU WINNNN Congratsssssssss!!!")

            else:
                    print(f" Invalid Input ")

            chance += 1 
            if(chance <5):
                    print(f"\n \t\t You have {5-chance} Chance Left \n")
            else :
                    print("\n \t\t Your chances are over ")

    else :
        break

'''

 -------  We are using random module and some conditions    --------

randint(): The randint() function in Python's random module returns a random integer number selected from a specified range. It takes two arguments: a lower bound (inclusive) and an upper bound (inclusive). The function then returns a random integer within this range.
random_number = random.randint(lower_bound, upper_bound)



What Customization we can do further ????????????????

1--> We can check input value whether user entered number or String Using try Catch block

2--> We can take user choice lower_bound and upper_bound.

3--> We can provide user choice option that they wanna play more or wanna exit.

4--> Any other???????????
'''