# #walrus operator
# if(n:=len([1,2,3,4,5]))>3:
#     print(f"List is too long {n} elements expected<=3")

# # Get a list of numbers from the user
# nums = input("Enter numbers separated by spaces: ").split()

# # Use the walrus operator to assign and check length in one line
# if (n := len(nums)) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")
# else:
#     print(f"List is acceptable ({n} elements)")



# def matchcase(status):
#     match status:
#         case 200:
#             return 'ok'
#         case 404:
#             return 'emergency'
#         case 500:
#             return 'unknown server error'
#         case _:
#             'unknown status'
# print(matchcase(500))



# try:
#     a=int(input("enter the number "))
#     print(a)

# except ValueError as v:
#     print("heyyy")
#     print

# except Exception  as e:
#     print(e)


# a=int(input("enter the number"))
# b=int(input("enter the number"))
# if(b==0):
#     raise ZeroDivisionError("A number cannot be devided by zero")
# else:
#     print(f"the division of a/b is {a/b}")

# a=89
# def fun():
#     global a
#     a=3
#     print(a)
# fun()
# print(a)


# a=89
# def fun():
#     # global a
#     a=3
#     print(a)
# fun()
# print (a)



# l=[]
# n=int(input("how many items you want to enter"))
# for i in range(n):
#     item=int(input(f"enter the {i+1} number"))
#     l.append(item)
# print(l)

# l=[4,5,6,3]
# index=0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index+=1

# #rather i can write like this

# for index,item in enumerate(l):
#         print(f"the item number at index {index} is {item}")


# try:
#     with open("1.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# l=[1,2,3,4,5,4,5,67,9]
# for i,item in enumerate (l):
#     if i==2 or i==4 or i==6:
#         print(item)


# n=int(input("enter the number you want the table of"))
# table=[n*i  for i in range(1,11)]
# print(table)

# l=[]
# n=int(input("enter the number you want the table of"))
# for i in range (1,11):
#     a=n*i
#     l.append(a)
# print(l)

# n=int(input("enter the number you want to enter the table of"))
# table=[n*i for i in range (1,11)]
# with open("2.txt","a") as f:
#     f.write(f"Table of {n}:{str(table)}\n")


# l=[1,2,3,4,5]
# squares=[]
# # square=lambda x:x*x
# # sqlist=map(square,l)
# # print(list(sqlist))


# for i in l:
#     a=i*i
#     squares.append(a)
# print(squares)


