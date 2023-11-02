'''ex=1.23+2.80
print(round(ex,2))
#string 
ex1="apricots"
print(ex1[:3])
print(ex1[2:5])
print(ex1[4:])

connected="r2"+"_"+"d2"
print(connected)
print(connected[3])
print(connected[1:4])

unchanged="forrest gump"
slice=unchanged[6:]
print(slice)
print(unchanged[10])

#type() Function
ex2=True
ex3=10
ex4=45.36
ex5= 'a'
ex6="ASDF"
print(type(ex2))
print(type(ex3))
print(type(ex4))
print(type(ex5))
print(type(ex6))

#escape sequences
print("ashish\tkuldeep")
print("ashish\nkuldeep")
print("ashish kuldeep\\.")
print('"when I said\' Immediatly,\' I ment today!" said king soul"')
print("\"Do or do not there is no try.\"")

print("*******\n *****\n  ***\n   *")

#input() Function
name=input("What is your name:")
age=input("Enter your age:")
print("Your name is "+name+".Your name is "+age+".")

#int() Function
use_int=int(input("plese enter an integer:"))
print(use_int)
print(type(use_int))

use_int = input("Please enter an integer.")
print(int(use_int) + 10)

#float() Function
use_float=float(input("Enter the number:"))
print(use_float)
print(type(use_float))

#function()
def function_name():
    print(2+2)
function_name()

#function with parameter
def function_name(parameter):
    print(parameter+2)
function_name(8)

#multiple parameters
first_str="The number"
def function_name(p1,p2,p3):
    print(p1+ str(p2) +p3)
function_name(first_str, 5, "is an integer")

def name_printer(user_name):
    print(user_name)
name = input("Please enter your name:")
name_printer(name)

def default_example(num1=7, num2=8):
    print(num1*num2)
default_example()

def default_example(num1=7, num2=8):
    return num1*num2
print(default_example()+44)

length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet.")) 
def prism_vol(l, w, h):
    return l * w * h 
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")

#celsius to Fahrenhit
celsius = int(input("Please enter an integer value for degrees celsius. "))
def fahrenheit(cel):
    return (18 * cel + 320) / 10
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
    
#Fahrenheit to celsius   
Fahrenheit = int(input("Please enter an integer value for degrees Fahrenheit. "))
def celsius(far):
    return ((1.8 * far + 32), 1)
print("The celsius equivalent of " + str(Fahrenheit) + " degrees Fahrenheit is " + str(celsius(Fahrenheit)) + ".")
    
#moduls 
#generic import
import random
print(random.randint(1,20)

#function import
from random import randint
print(randint(10,20))

#universal import
from random import *
print(random())

from random import randint
fuel = randint(10, 25)
miles = randint(200, 400)
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
print("The car can travel " + str(miles) + " miles on a full tank.")'''

a=int(input("enter a:"))
b=int(input("enter b:"))
def add(x,y):
   return x+y
print("the addition of "+str(a)+" and "+str(b)+" is "+str(add(a,b))+".")