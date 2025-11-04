# class employees:
#     language="py" #this is an class attributte
#     salary="120000" 
# harry=employees()
# harry.name="Harish"
# print(harry.name,harry.language,harry.salary)
# rohan=employees()
# rohan.name="rocky bhai" #this is an instant attribute
# print(rohan.name,rohan.language,rohan.salary)

#if there is no instant attribute than it will take as given in class attribute

# class employees:
#     language="py" #this is an class attributte
#     salary="120000" 
#     # def getinfo(self):
#     #     print(f"the language  is {self.language}.The salary is {self.salary}")

#     #     @staticmethod
#     #     def greet():
#     #         print("good morning")
#     #     greet()
#     def __init__(self,name,salary,language):
#         self.name=name
#         self.salary=salary
#         self.language=language




# rohan=employees("Rohit",140000,"Javascript")
# # rohan.name="rocky bhai" #this is an instant attribute
# print(rohan.name,rohan.language,rohan.salary)
# # rohan.getinfo()



# class programmer:
#         company="Microsoft"
#         def __init__(self,name,salary,pin):
#             self.name=name
#             self.salary=salary
#             self.pin=pin
# p=programmer("Rashmi Shaw",2300000,"1002001")
# print(p.name,p.salary,p.pin)



# class calculator:
 
#      def __init__(self,n):
#         self.n=n
#      def square(self):
#         print(f"the square of {n} is {self.n*self.n}")

# n=int(input("enter the number"))
# a=calculator(n)
# a.square()



# import random
# class train:
#     def __init__(self,trainNo):
#         self.trainNo=trainNo


#     def book(self,fro,to):
#         print(f"ticket is booked in train no:{self.trainNo} from {fro} to {to}")
#     def getstatus(self):
#         print(f"ticket having train no:{self.trainNo} is runnig succesfully")
        
#     def getfare(self,fro,to):
#         print(f"ticket is booked in train no:{self.trainNo} from {fro} to {to} is {random.randint(222,1999)}")

# t=train(122001)
# t.book("Delhi","Kanpur")
# t.getstatus()
# t.getfare("Delhi","Kanpur")


# class employee:
#     company="itc"
#     def show(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary} ")
# class programmer(employee):
#     company="itc infotech"
#     def showlanguage(self):
#         print(f"the name is {self.name} and he  is good with {self.language}")
# a=employee()
# b=programmer()
# print(a.company,b.company)

# class number:
#     def __init__(self,n):
#         self.n=n
#     def __add__(self,num):
#         return self.n+num.n


# n=number(1)
# m=number(2)
# print(n+m)


# class twodimensionvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         return f"two dimension vector is {self.i}i+{self.j}j "
# class threedimensionvector(twodimensionvector):
#     def __init__(self,i,j,k):
#         # self.i=i
#         # self.j=j
#         super().__init__(i,j)
#         self.k=k
#     def shows(self):
#         return f"thre dimension vector is {self.i}i+{self.j}j+{self.k}k "
# x=twodimensionvector(1,2)
# y=threedimensionvector(1,2,3)
# print(x.show()+"\n"+y.shows())




# class animal:
#     pass
# class pets(animal):
#     pass
# class dogs(pets):
#     @staticmethod
#     def bark():
#         print(
#             "bow bow"
#         )
# d=dogs()
# d.bark()



# class employee:
#     salary=234
#     increement=10
#     @property
#     def salaryafterincreement(self):
#          return(self.salary+self.salary*(self.increement/100))
#     @salaryafterincreement.setter
#     def salaryafterincreement(self,salary):
#         self.increement=((salary/self.salary)-1)*100

# e=employee()
# print(e.salaryafterincreement)
# e.salaryafterincreement=257.4
# print(e.increement)


class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
        
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    
    def __str__(self):
        return  f"{self.r}+{self.i}i"
c1=complex(1,2)
c2=complex(3,4)
print(c1+c2)

