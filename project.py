import random
number=random.randint(1,100)
gueses=0
a=-1
while(a!=number):
    gueses+=1
    a=int(input("guess the number between 1-100:"))
    if(a>number):
        print("the lower number please ")
        gueses+=1
    elif(a<number):
        print("the higher number please")
        gueses+=1

    else:
        print(f"you have guessed the number {number} correctly in {gueses} attempts")
        
    


