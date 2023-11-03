'''print(8>7)
#if statement
num=int(input("enter number:"))
if num==4:
    print("number is true")
    
#if else statement
num=int(input("Enter the number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")
    
#nested if and else
gap=float(input("what was the applicant's grade point average?:"))
inst_app=input("Is the student going to be educated at an approved institution?")
if gap>=3.7:
    if inst_app=="yes":
        print("The applicant qualifies for a low APe student loan")
    else:
        print("The applicant does not qualify since they have not been accepted into an approved institution")
else:
    print("the applicant did not have high enough grades to qualify")
score = int(input("Please enter the student's score. "))''' 
 
#nested if else
score=int(input("Enter score:"))
if score >= 90:
    print("This student's score of " + str(score) + " is an A.")

elif score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    
elif score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        
elif score >= 60:
                print("This student's score of " + str(score) + " is a D.")
else:
                print("This student's score of " + str(score) + " is a F.")

'''#elif statement
from random import randint
one_to_ten = randint(1, 10)
 
if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")'''