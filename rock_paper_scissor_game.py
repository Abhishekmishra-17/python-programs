import random
print('WELCOME IN "ROCK PAPER SCISSOR" GAMING WORLD')
print("Winning Rules of the Rock paper scissor game as follows: \n"+"Rock vs paper->paper wins \n"+ "Rock vs scissor->Rock wins \n"+"paper vs scissor->scissor wins \n") 
Rank_countuser=0
Rank_countcomputer=0
while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
    choice = int(input("User turn:"))
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: "))
    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor' 
    print("user choice is: " + choice_name) 
    print("\nNow its computer turn**********") 
    comp_choice = random.randint(1, 3)  
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3)  
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
    print("Computer choice is: " + comp_choice_name) 
    print(choice_name + " V/s " + comp_choice_name) 
    if((choice == 1 and comp_choice == 2) or(choice == 2 and comp_choice ==1 )): 
        print("<=paper wins => ", end = "") 
        result = "paper"
    elif((choice == 1 and comp_choice == 3) or(choice == 3 and comp_choice == 1)): 
        print("<=Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("<=scissor wins =>", end = "") 
        result = "scissor"
    if result == choice_name: 
        print("<== User wins ==>")
        Rank_countuser+=1
    else: 
        print("<== Computer wins ==>")
        Rank_countcomputer+=1
    ans=input("Do you want to continue(y/n)")
    if(ans=='N' or ans=='n'):
       break
    elif(ans=='y' or ans=='Y'):
        continue
    else:
        print("Enter the valid key")
        break
if( Rank_countuser>Rank_countcomputer):
    print("congratulations! You are winner\n\t"+"your score is:",Rank_countuser,"out of",Rank_countuser+Rank_countcomputer)
elif(Rank_countuser==Rank_countcomputer):
    print("Game is drawn\n\t"+"your score is:",Rank_countuser,"out of",Rank_countuser+Rank_countcomputer)
else:
    print("You are looser\n\t"+"your score is:",Rank_countuser,"out of",Rank_countuser+Rank_countcomputer)

print("\nThanks for playing") 
