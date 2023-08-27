'''
Status ==> Not Completed

'''

# Some references are attached at the bottom

import random
import sys


def Play ( ) :
    user_choice = int(input('''\n Enter your choice :

    \t\t  0 - Rock 
    \t\t  1 - Paper 
    \t\t  2 - Scissors

    ''')  ) # taking users input for rock paper scissors
    computer_choice = ['rock', 'paper', 'scissors']

    if (user_choice ==1) :  
        user_choice =  "rock"
      

    elif (user_choice ==2) : 
        user_choice =  "paper"  
       

    elif (user_choice ==3) :
        user_choice = "scissors"   
      

    else :
        print("Invalid User choice")

    listIndex = random.randint(0,len(computer_choice)-1) # will select from 0 to len-1 (inclusive)
    compPicked = computer_choice[listIndex]
    # print(f"computer coice: {compPicked}")
    #  now lets compare the choice and select winner

    if (user_choice in ['rock', 'paper', 'scissors']):
            if (user_choice== "rock" and (compPicked == "paper")):
                print(f'you loose,computer select paper and you selected {user_choice}')

            elif (user_choice== "rock" and (compPicked == "scissors")):
                print(f'you Win,computer select scissors and you selected {user_choice}')

            elif (user_choice== "paper" and (compPicked == "rock")):
                print(f'you Win,computer select rock and you selected {user_choice}')

            elif (user_choice== "paper" and (compPicked == "scissors")):
                print(f'you loose,computer select scissors and you selected {user_choice}')

            elif (user_choice== "scissors" and (compPicked == "rock")):
                print(f'you loose,computer select rock and you selected {user_choice}')

            elif (user_choice== "scissors" and (compPicked == "paper")):
                print(f'you Win,computer select paper and you selected {user_choice}')

            else :
                print('tie,you both selected same')
    else:
            pass
    


def Exit ( ) :
    sys.exit("See you Again")


print("\n\n \t\t ******************Rock , Paper  , Scissors Game Start ***********************")

while(True):
    PlayOrQuit = int ( input ("\n \t\t Press 1 for Play and 0 for Exit :"))
    print("\n")
    if (PlayOrQuit == 1) :
            Play()
    if (PlayOrQuit==0):
        Exit()
    else :
        print("please enter 1 or 0 ")


'''
 -------  We are using ------
Rule:
The rules state that rock smashes scissors, scissors cuts paper, and paper covers rock. So, rock wins over scissors, scissors win over paper and paper wins over rock.
-->random module use to generate random numbers
--> sys modul is used to use sys.exit() to quite program

What Customization we can do further ????????????????

--> you can add try , except(i.e catch) to avoid error if user enters string

--> you can give chance to user : how many choices they have and count their wins.Whoever won more time than other will be the final winner.
--> can be use Oops concept later
--> can be use Oops concept later
'''