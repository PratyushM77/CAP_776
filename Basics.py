# import pyjokes
# import pyttsx3
# import os
# import random
# import mymodule
# import datetime
# import math

# joke = pyjokes.get_joke()
# print(joke)
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.''')

# engine = pyttsx3.init()
# engine.say("Hola yo soy pratyush mucho gusto!!")
# engine.runAndWait()

# directory_path = '/New folder'
# contents = os.listdir(directory_path)

# for items in contents:
#  print(items)

# a = 1 # a is an integer
# b= 2.8 # b is an floating point number
# c = "Pratyush" # c is an string
# d = False # d is an boolean
# e = None # e is an none type variable
# a = 10.2
# print(type(int(a)))
# print(a)1

# a = int(input("Enter you number ")
# z =) 10
# if int(a) % int(z) == 0: print("a is divisble by z")

# name = "Pratyush Mishra"
# age = 22
# print(len(name))
# print(name[0:4])
# print(name.split('i'))
# stat = f"My name is {name} and i am {age} years old!!"
# print(stat)

# list = ["Pratyush", False, "21",False, 9, 4.05]
# print(list.count(False))
# print(list)
# list1 = []

# print("Hello World!", end=" ")
# print("I will print on the same line.")

# q1 = int(input("Write marks of student.."))
# list1.append(q1)
# q2 = int(input("Write marks of student.."))
# list1.append(q2)
# q3 = int(input("Write marks of student.."))
# list1.append(q3)
# q4 = int(input("Write marks of student.."))
# list1.append(q4)
# q5 = int(input("Write marks of student.."))
# list1.append(q5)
# q6 = int(input("Write marks of student.."))
# list1.append(q6)

# list1.sort()
# print(list1)
# list1 = [1,2,3]
# list2 = ["pratyush","marry",12]
# list  = list1 *2
# print(list)
# i = 0
# while(i<=50):
#     print(i)
#     i+=1
# for i in range(1,10,3):
#     print(i)

# inp = int(input("Enter your Number"))
# for i in range(inp,inp*11,inp):
#     print(i)

# for i in range(1,11):
#     print(f"{inp} X {i} = {inp*i}")
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*", end=" ")
#     print()

# n= 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(n,0,-1):  100,9
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()
# n=10
# for i in range(10,0,-1):
#    rev =  f"mult of {n} X {i} is {n*i}"
#    print(rev)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n= 5
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*", end=" ")
#     print()
# def natnum(n):
#     if(n==1 or n==0): return 1
#     return n + natnum(n-1)


# n = int(input("Write a number..."))
# print(natnum(n))

# """ a= append ; w = write ; r = read"""

# f = open("text1.txt", "a")

# f.write("i am good ")
# f.close()

# with open("text1.txt","r") as f:
#     print(f.read())

# save = random.randint(1,50)
# print(save)
# c = "twinkle"
# with open("poems.txt","r") as f:
#     con = f.read()
#     if(c in con):
#         print("yes it contains twinkle")
#     else:print("it doesnt contains")


# def game():
#     print("Game started")
#     with open("hiscore.txt", "r") as f:
#         save = f.read()
#     num = random.randint(1, 50)
#     print(num)
#     if (int(save) < num or save == ""):
#         with open("hiscore.txt", "w") as wr:
#             wr.write(str(num))

# game()


# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"Table of {n} X {i} = {n*i}\n"
#         with open(f"tables/table_{n}.txt", "w") as wr:
#             wr.write(table)


# for i in range(2, 21):
#     generateTable(i)
# c = "Donkey"
# with open("test.txt","r") as t:
#     save = t.read()

# new = save.replace(c,"#"*len(c))
# with open("test.txt","w") as wr:
#     wr.write(new)
# py = "python"
# with open("test.txt") as f:
#     contains = f.readlines()
# num = 1
# for line in contains:

#     if py in line:

#         print(f"Yes it contains python in line {num}")
#         # print(num)
#     num += 1
# else:
#     print("it doesnt contains python")

# class pyt:
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age
#     def showdetails(self):
#         return f"My name is {self.name} and I am {self.age} years old"


# class js(pyt):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def say(self):
#         return f"I am from say func.{self.showdetails()}"

# p1 = js("Pratyush",21)
# print(p1.say())


# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def info(self):
#         return f"Brand: {self.brand}"


# class Bike(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def details(self):
#         return f"{self.info()}, Model: {self.model}"


# b1 = Bike("Royal Enfield", "Classic 350")
# print(b1.details())

# class Account:
#     def __init__(self,balance,account_num):
#         self.balance= balance
#         self.account_num = account_num
#     def debit(self,amount):
#         self.balance-=amount
#         print(f"{amount} Money has been debited your balance is {self.balance}")
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"{amount} Money has been credited your balance is {self.balance}")

#     def printing_bal(self):
#         print(f"You have {self.balance} in your account ending with {self.account_num}")


# s1 = Account(40000,123456)
# s1.debit(10000)
# s1.credit(1)

# list1 = [1,2,3,4,5]
# list1.extend((6,))
# print(list1)

# print(mymodule.person("Pratyush"))
# print(dir(mymodule))

# x = 3.14159265

# print(round(x,1))
# print(x)

# x = "python is ok"
# print(x[::-1])

# x = 3.14159265
# print(f"The price is {0:.2f}")

# print(pyjokes.get_joke())


# def generate():
#     save = 0
#     save = int(random.randint(1, 100))
#     print(save)
#     inp = int(input("Guess a number "))
#     # if(save!=inp):

#     while save != (inp):
#         if save > inp:
#             print("Guess a higher number ")
#             inp = int(input("Guess a number "))
#         else:
#             print("Guess a lesser number ")
#             inp = int(input("Guess a number "))

#     print("Golazo!! You guessed it Right.")


# generate()

# for x in range (1,11):
#     print(x)

# n = int(input("Write a number so i can give you table: "))
# with open("Tables.txt","a") as f:
#     for i in range(1,11):
#         print("\n")
#         f.write(f"Multiplication of {n} X {i} = {n*i}\n")


# print("Enter a Pixel: ")
# pixel = int(input())
# if(pixel>=0 and pixel<=255):

# Q1

# if(pixel<=75 ):
#     print("Pixel is Dark")
# else:
#     print("Pixel is Bright")


# Q2

# if(pixel>127):
#     print("Pixel is Bright")
# else:
#     print("Pixel is Dark")


# Q3
# if(pixel>=192):
#     print("Pixel is Bright")
# elif(pixel>=130):
#     print("Pixel is Medium Bright")
# elif(pixel>=64):
#     print("Pixel is Medium Dark")
# else:
#     print("Dark")


# Q4

# if(pixel>=80 and pixel<=180):
#     print("Pixel is a Part of Image")
# else:
#     print("Pixel is not a part of Image")

# else:
#     print("Enter a valid pixel Between 0 and 255")


# list_1 = [15,40,75,110,130,250,185,200,230]

# i=0
# count_1 = 0
# count_2 = 0
# max = list_1[0]

# for num in list_1:
#     if(num>=128):
#         print(f"{num} is the brighter pixel")
#         count_1 = count_1+1

#     else:
#         print(f"{num} is the darker pixel")
#         count_2 = count_2+1


# for num in list_1:
#     if(num>=max):
#         max = num

# percentage =  (count_1/len(list_1))*100


# print("Percentage is :",float(percentage),"%")
# print("Max num is",max)
# print("Total brighter count :",count_1)
# print("Total darker count :",count_2)


# Problem Statement 1 || Date - 27/8/26

# Breathing_prob = False
# Fever = True
# Temp = 39
# Cough = True
# if(Breathing_prob):
#     print("Admit the patient Urgently")
# else:
#     if(Temp>37):
#         print("Patient having Fever")
#         if(Cough):
#             # print("Patient having cough")
#             print("Patient suffering from Respiratory infection probably Flu")

#         else:
#             print("Unknown")

#     else:
#         if(Cough):
#             print("Patient having Cold")
#         else:
#             print("Unknown")

# Problem Statement 2 || Date - 02/9/26


print("In how many subjects you appeared?")
inp = int(input())
# list  = []
dict = {}
for i in range(inp):
    print("Enter Subject Name: ")
    usersub = str(input())
    print("Enter Marks: ")
    usermarks = int(input())
    dict[usersub] = usermarks


def calculate_total():

    return sum(dict.values())


def calculate_average(total):
    return total / inp


def calculate_grade(average):

    if average > 90:
        print("Grade: A+")
    elif average > 80:
        print("Grade: A")
    elif average > 70:
        print("Grade: B")
    elif average > 60:
        print("Grade: C")
    elif average > 50:
        print("Grade: D")
    else:
        print("Grade: F")


def calculate_status(total):
    if (total / (inp * 100)) * 100 > 33:
        print("Pass")
    else:
        print("Fail")


total = calculate_total()
average = round(calculate_average(total), 2)
print("Total marks you got:", total)
print("Average marks you got:", average)
grade = calculate_grade(average)

calculate_status(total)
