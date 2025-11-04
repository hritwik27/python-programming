# import pyjokes
# jokes=pyjokes.get_joke()
# print(jokes)


# #use triple string to print the multiline
# print("""Here are the lyrics to the poem:
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are!
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# Twinkle, twinkle, little star,
# How I wonder what you are!
# In the dark blue sky you keep,
# And often through my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are!""")

# import pyttsx3
# # Initialize the TTS engine
# engine = pyttsx3.init()
# # Convert text to speech
# engine.say("Get lost bitch   ")
# # Wait for the speech to finish
# engine.runAndWait()




# print("True and False",True and False)
# print("True and True",True and True )
# print("False and True",False and True)
# print("False and False",False and False)



# a="31.2"
# # print(type(a))
# a=float(a)
# print(type(a))



# a=int( int(input("enter the first number:"))
# b=int( int(input("enter the second number:"))
# c=a+b
# print("the sum of a+b is",c)

# a=int( int(input("enter the first number:"))
# b=int( int(input("enter the second number:"))
# c=a%b
# print("the remaider of a % b is",c)


# a=int( int(input("enter the first number:"))
# # print("the square of number is ",a**2)
# name="harry"
# nameslice=name[0:2]
# print(nameslice)
# character=name[1]
# print(character)
# # print(name[-4:-1])
# word="hritwikshaw"
# print(word[0: :3])
# print(len(word))
# print(word.endswith("haw"))
# print(word.replace('shaw','sharma'))
# # print(word.upper())

# name= int(input("enter your name :")
# print(f"Good Afternoon {name}")

# letter='''dear |Name|
# You are selected!
# <|Date|>'''
# print(letter.replace("|Name|","Ujjwal").replace("<|Date|>","24 September 2028"))





# name="Harry is a good boy"
# print(name.find("good boy"))
# #if ther  is any double space it will return -1
# print (name.replace("Harry","Hritwik"))
#strings are immutble which means that you cannot change them by executing functions on them


# str=["Harry","Satwik","Ujjwal","Hritwik"]
# str[0]="DEVYANSH"
# print(str)
# print(str[1:3])
# str.append("Devyansh Gupta")
# print(str)
# l1=[1,2,6,4,9,3,-12,0]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(3,57)
# print(l1)
# l1.pop(3)
# print(l1)
# value=l1.pop(3)
# print(value)
# l1.remove(0)
# print(l1)
# tupple=(1,2,3,4,5)
# print(tupple.count(5))
# print(tupple.index(5))
# print(len(tupple))
# sliced=tupple[:3]
# print(sliced)











# Marks=[]
# f1= int(input("Enter the Marks :"))
# Marks.append(f1)
# f2= int(input("Enter the Marks :"))
# Marks.append(f2)
# f3= int(input("Enter the Marks :"))
# Marks.append(f3)
# f4= int(input("Enter the Marks :"))
# Marks.append(f4)
# f5= int(input("Enter the Marks :"))
# Marks.append(f5)
# f6= int(input("Enter the Marks :"))
# Marks.append(f6)
# print(Marks)

# print(Marks.sort())
#sorting does not happen because thre list contain the value as string

# l=[24,3,43,4,32,2]
# print(sum(l))

# a=(7,0,8,0,0,9)
# n=a.count(0)
# print(n)



# marks={"key":"value","Harry":100,"satwik":98}
# print (marks)
# print(marks["Harry"])
# # print(marks["key"])
# # print(marks.item())
# # print(marks.key())
# # print(marks.value())
# marks.update({"Harry":99})
# print(marks)
# print(marks.items())
# # print(marks.get("Harry"))


# print(marks["Harry2"]) returns error
# print(marks.get("Harry2")) //retuns none




# s={} #it creates an empty dictionaries
# s=()# it creates an empty set

#sets are used to create the collection of numbers or words that are not repeated thus no repeatition allowed

# a={1,2,3,3,2,1,5,67,3}
# print(a)
# a.add(100)
# print(a,type(a))
# s1={1,2,3,4,5,6}
# s2={9,8,7,6,5,4,3,2,1}
# print(s1.intersection(s2))
# print(s1.issubset(s2))
# print(s2.difference(s1))


# words={
#     "madad":"help",
#     "kursi":"chair"
# }
# word=input("enter the word you wnat the meaning of:")
# print(words[word])


# s=set()
# n=int(input("enter the number:"))
# s.add(int(n))

# n=int(input("enter the number:"))


# n=int(input("enter the number:"))
# s.add(int(n))

# n=int(input("enter the number:"))
# s.add(int(n))

# n=int(input("enter the number:"))
# s.add(int(n))
# print(s)






# d={}
# name=input("enter the name:")
# lang=input("enter the language:")
# d.update({name:lang})

# name=input("enter the name:")
# lang=input("enter the language:")
# d.update({name:lang})

# name=input("enter the name:")
# lang=input("enter the language:")
# d.update({name:lang})

# name=input("enter the name:")
# lang=input("enter the language:")
# d.update({name:lang})
# print(d)

# a=int(input("enter the number"))
# if(a>18):
#     print("you are legal")
# else:
#     print("not legal")


# l=["Harry","Hritwik","Satwik"]
# name=input("enter the name to check:")
# if(name in l):
#     print("true")
# else:
#     print("False")

# post=input("enter the post:")
# if("Harry".lower() in post.lower()):
#     print("this post is talking about harry")
# else:
#     print("this post is not talking about harry")

# i=1
# while(i<6):
#     print(i)
#     i+=1

# for i in range(0,7):
#     print(i)


# l=[1,"hritwik","shaw","Satwik","Shaw"]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i+=1

# for i in l:
#     print(i)

# for i in range(100):
#     if(i==34):
#         break
#     print(i) 

# for i in range(100):
#     if(i==13):
#         continue
#     print(i)

# n=int(input("enter the number "))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

# l=["Soham","Satwik","Harsh","Hritwik"]

# for name in l:
#     if(name.startswith("H")):
#         print(f"Hello {name}")
# n=int(input("enter the number "))
# i=1
# while(i<11):
#    print(f"{n}X{i}={n*i}") 
#    i+=1 


# n=int(input("enter the number"))
# fact=1

# for i in range(1,n+1):
#    fact=fact*i
# print(f"the factorial  of {n} is {fact}")

# n=int(input("enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1),end=" ")
#     print("")
    
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     if(i==1 or  i==n):
#         print("*"*n,end="")
        
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end=" ")
#     print("")
    # print(""*(n-i),end=" ")
    # print("*"*(i),end=" ")
    # print("")    

# n=int(input("enter the number"))
# for i in range(10,0,-1):
#     print(f"{n}X{i}={n*i}")




# def goodday(name,ending):
#     print("Good Day,"+ name)
#     print(ending)
#     return "bye"

# #goodday("Harry","thankyou")
# a=goodday("Harry","Thankyou")
# print(a)


# def average():
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     c=int(input("enter the number"))
#     avg=a+b+c/3
#     print(avg)
#     return a
# a=average()



# def greatest(a,b,c):
#     if(a>b and a>c):
#         print("a is greatest")
#         return a
#     elif(b>c and b>a):
#         print("b is greatest")
#         return b
#     else:
#         print("c is greatest")
#         return c

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# print(greatest(a,b,c))


# def ftoc(f):
#     c=5*(f-32)/9
#     return c

# f=int(input("enter the farenhite"))
# c=ftoc(f)
# print(f"{c} degree celsius")


# n=int(input("enter the number"))
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n
# print(sum(n))


# n=int(input("enter the nuber of stars"))
# def star(n):
#     if(n==0):
#         return
#     print("*"*n)
#     star(n-1)
# star(n)


# f=open("harry.txt")
# data=f.read()
# print(data)
# f.close()


# st="hey harry you are amazing"
# f=open("hritwik.txt","w")
# data=f.write(st)
# print(data)
# f.close()

# f=open("harry.txt")
# # lines=f.readline()
# # while(lines!=""):
# #     print(lines)
# #     lines=f.readline()
# f.close()


# st="satwik is also a good boy"
# f=open("harry.txt","a")
# f.write(st)
# f.close()


# with open("hritwik.txt") as f:
#     print(f.read())




    
    
# import random

# def game():
#     print("You are playing the game..")
#     score = random.randint(1, 62)
#     # Fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score: {score}")
#     if(score > hiscore):
#         # write this hiscore to the file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score
# game()

# import random
# def game():
#     print("you are playing a game")
#     score=random.randint(1,100)
#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"your score:{score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
# game()


# def gentable(n):
#     table=""
#     for i in range (1,11):
#         table+=f"{n}x{i}={n*i}\n"
#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)
        
# for i in range(2,21):
#     gentable(i)

# word="donkey"
# with open("file.txt") as f:
#     content=f.read()

# contentnew=content.replace(word,"####")
# with open("file.txt","w") as f:
#     f.write(contentnew)

# words=["bsdk","bkl","suar"]
# with open("file.txt") as f:
#     content=f.read()

# for word in words:
#     content=content.replace(word,"#"*len(word))

# with open("file.txt","w") as f:
#     f.write(content)

# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self,other):
#         result=(self.x+other.x,self.y+other.y,self.y+other.y)
#         return result
#     def __mul__(self,other):
#         result=(self.x*other.x+self.y*other.y+self.y*other.y)
#         return result
#     def __str__(self):
#         return f"Vector({self.x},{self.y},{self.z})"
# v1=vector(1,2,3)
# v2=vector(4,5,6)
# v3=vector(7,8,9)
# print(v1+v2)
# print(v1*v2)

# print(v1+v3)
# print(v1*v3)







     



