# import random
# computer=random.choice([-1,0,1])
# yourchoice=input("enter your choice").strip().lower()
# yourdict={"snake":-1,"water":0,"gun":1}
# compdict={-1:"snake",0:"water",1:"gun"}
# you=yourdict[yourchoice]
# print(f"you chose {compdict[you]}\n computer chose{compdict[computer]}")
# if(computer == you):
#     print("It's a draw")

# else:
#     if(computer == 1 and you == 1):
#         print("You win!")

#     elif(computer == -1 and you == 0):
#         print("You Lose!")

#     elif(computer == 1 and you == -1):
#         print("You lose!")

#     elif(computer == 1 and you == 0):
#         print("You Win!")

#     elif(computer == 0 and you == -1):
#         print("You Win!")

#     elif(computer == 0 and you == 1):
#         print("You Lose!")

#     else:
#         print("Something went wrong!")


import random

computer = random.choice([-1, 0, 1])

yourchoice = input("Enter your choice (snake, water, gun): ").strip().lower()

yourdict = {"snake": -1, "water": 0, "gun": 1}
compdict = {-1: "snake", 0: "water", 1: "gun"}

if yourchoice not in yourdict:
    print("Invalid choice! Please enter snake, water, or gun.")
else:
    you = yourdict[yourchoice]

    print(f"You chose {compdict[you]}\nComputer chose {compdict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 0) or (computer == 0 and you == 1) or (computer == 1 and you == -1):
        print("You lose!")
    else:
        print("You win!")
