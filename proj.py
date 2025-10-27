# def get_choices():
#     player_choice="rock"
#     computer_choice="paper"

#     return computer_choice 

# # def greeting():
# #     return "hi"

# # response=greeting()
# # print(response)

# choices=get_choices()
# print(choices)  
# import random 

# def get_choices():
#     player_choice=input("enter the choice (rock,paper,scissor :")
#     options=["rocks","paper","scissor"]
#     computer_choice=random.choice(options)
#     choices={"player":player_choice,"computer":computer_choice}

#     return choices

# choices=get_choices()
# print(choices)


# dictionaries used to store the data value of key and its value
# key : value



# line01="*************" #header/footer
# line02="*           *" #reuse
# line03="*  welcome! *" 
# #starts with a blank file
# print('')
# print(line01)
# print(line02)
# print(line03)
# print(line02)
# print(line01)



# print(24/5)
# print(24//5)
# print(24%5)
# print(2**3)
# meaning=42
# meaning+=1
# print(meaning)

# meaning=42
# print(" ")
# if meaning > 10:
#     print("right on")
# else:
#     print("not today")


#ternary operator
#print('right on')if meaning > 10 else print('not today')




#DARTA TYPE
# first="dave"
# last="gray"
# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))

#construct a function

# pizza=str("peproni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

#concatenation

# fullname= first+ last
# print(fullname)
# fullname += "!"
# print(fullname)

#CASTING A NUMBER
# decade=str(1980)
# print(type(decade))
 
# statement="ilike the rock music from the"+" "+decade+"s"
# print(statement)

#multiline

# multiline= '''
# hey how are you?
#                   i was just checking in
# all good?


# # '''
# print(multiline)




#escaping special characters


# sentence= 'I\'m back at work! \t hey!\n\n where\'s this at located'
# print(sentence)



#string methods


# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title()) #make every first letter capital
# print(multiline.replace("good","ok"))
# print(multiline)


# print(len(multiline))
# multiline='             '+ multiline
# print(len(multiline.strip()))


#build a menu
# title="menu".upper()
# print(title.center(20,"="))
# print("coffee".ljust(16,".")+"$1".rjust(4))


#INDEXING
# print(first[1])
# print(first[-1])
# print(first[1:-1])


# #casting string to a number
# zipcode="1001"
# zipcode=int(zipcode)
# print(type(zipcode))

#error if you attempt to cast incorrect data 
#zip-value=int(new york)



# import sys
# import random
# from enum import Enum 
# class RPS(Enum):
#     ROCK=1
#     PAPER=2
#     SCISSOR=3
# # print(RPS(2))
# # print(RPS.ROCK)
# # print(RPS["ROCK"])
# # print(RPS.ROCK.value)
# player_choice=input("enter the choice\n1 for ROCK \n2 for PAPER \n3 for scissor\n")
# playerchoice=int(player_choice)
# if playerchoice<1 or playerchoice>3:
#     sys.exit("you must enter 1,2 or 3")

# computerchoice=random.choice("123")
# computer=int(computerchoice)
# print("")
# print("you chose"+ " "  +str(RPS(playerchoice)).replace("RPS."," ")+"")
# print("python chose"+" "+ str(RPS(computer)).replace("RPS."," ")+"")
# print("")
# if(playerchoice==1 and computer==3):
#     print("🍾you win")
# elif(playerchoice==2 and computer==1):
#     print("🍾you win")
# elif(playerchoice==3 and computer==2):
#     print("🍾you win")
# elif(playerchoice==computer):
#     print("😲it's draw")
# else:
#     print("🐍python wins")



#lists and tupples


# users=["dave","john","safra"]
# data=["hritwi",18]
# emptylist=[]
# print("dave" in users)
# print(users[0])
# print(users[-2])
# print(users[-1])
# print(users.index('safra'))
# print(users[1:])
# print(users[-3:-1])
# print(len(users))
# users.append('elsa')
# print(users)
# users+=["jason"]
# print(users)
# users.extend(['robert','hritwik'])
# print(users)
# # if we do not put bracket in jason we get each letter of jason in the list
# #we cannot put direct list name in extend command
# users.insert(-4,'bob')
# print(users)
# users[2:2]=['eddie','alex']
# print(users)
# print(" ")
# users[1:3]=['robert','jpj']
# print(users)
# users.remove('bob')
# print(users)
# print(users.pop())
# print(users)
# del users[0]
# print(users)

# print(" ")
# users.sort(key=str.lower)
# users.sort()
# print(users)

# nums=[4,5,10,7,8]
# nums.reverse()
# print(nums)

# # nums.sort(reverse=True )
# # print(nums)

# print(sorted(nums,reverse=True))
# print(nums)

# numscopy= nums.copy()
# mynums=list(nums)
# mycopy=nums[:]
# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)
# print(nums)

# mytuple=tuple(('dave',42,True))
# anothertuple=(1,4,2,8)
# print(mytuple)
# newlist=list(mytuple)
# newlist.append('neil')
# newtuple=tuple(newlist)
# print(newtuple)


# #dictionaries
# band= {
#     "vocals": "plant",
#     "guitar":"page"
# }
# band2=dict(vocals="grass",guitar="sitar")
# print(band)
# print(band2)
# print(type(band))
# print(len(band))
# #acces item in dictionaries
# print(band.get("guitar"))
# print(band.values())
# print(band.keys())


# #list of key/value pairs as tuples
# print(band.items())

# #verify key exist
# print("guitar" in band)
 
# #change value in dictionaries 
# band["vocals"]="coverdale"
# band.update({"bass":"jpg"})
# print(band)

# #remove item
# print(band.pop("bass"))
# print(band)




# band["drums"]="bonham"
# print(band)

# print(band.popitem())
# print(band)

# #delete or clear item

# band["drums"]="bonham"
# print(band)
# del band["drums"]
# print(band)

# band2.clear()
# print(band2)
 
# #copy dictionaries
# band2 = band #create refrence
# print("bad copy")
# print(band2) 
# print(band) 
# band2["drums"]="dave"
# band2.update({"drums":"dave"})
# print(band)

# band2=band2.copy()
# band2.update({"drums":"dave"})
# print(band2)
# value=1
# while value < 10:
#       print(value)
#       if value==5:
#             break
#       value +=1


# value=1
# while value < 10:
#       print(value)
#       if value==5:
#             continue
#       value +=1


# value=1
# while value < 10:
#       value +=1
      
#       if value==5:
#             continue
#       print(value)





# import random 
# n=random.randint(1,100)
# print("you have 7 chances ")
# for j in range(0,7):
#     print((7-j),"chances are remaining")
#     c=int(input("enter the number "))
#     if c==n :
#            print("correct")
#            break
#     elif c>n:
#            print("to High ")
           
#     else : 
#            print("to low ")

# if c!=n :
#         print("failed")
        
# else :
#       print("you guessed it right you are smart ")












































