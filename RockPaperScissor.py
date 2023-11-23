#Program for Rock Papar Scissors Game in python 
import random

print("Welcome to Rock Paper Scissors game") 
while True:
     
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n ")
     
    # take the input from user
     
    choice=int(input("Enter your choice :"))
     
     
    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name= 'Paper'
    elif choice == 3:
        choice_name= 'Scissors'
    else:
        print("Default choice")
         
    # print user choice
    print('User choice is \n',choice_name)
    
    #Computer Choice
    comp_choice = random.randint(1,3)
     
    
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
         
     
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    elif comp_choice == 3:
        comp_choice_name = 'scissor'
    else:
        print("Default choice")

    print("Computer choice is \n", comp_choice_name)
    
    if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"

    # condition for winning      
    if (choice==1 and comp_choice==2):
        print('paper wins\n',end="")
        result='paper'
    elif (choice==2 and comp_choice==1):
        print('paper wins\n ',end="")
        result='Paper'
         
       
    if (choice==1 and comp_choice==3):
        print('Rock wins \n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins \n',end= "")
        result='rock'
         
    if (choice==2 and comp_choice==3):
        print('Scissors wins\n ',end="")
        result='scissor'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins\n ',end="")
        result='Rock'

     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("Its a tie ")
    if result == choice_name:
        print("User wins ")
    else:
        print("Computer wins ")

    print("Do you want to play again? (Y/N)")
    
    ans = input()
    if ans == 'N':
        break

print("Thanks for playing")
    

