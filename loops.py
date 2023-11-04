'''#loops
#while loop
no=1
while no<10:
    print(no)
    no+=1
    
#infinite loop  
no=1
while no<10:
    print(no)
 
#while loop   
dec_int = 10
while dec_int > 0:
    print(dec_int)
    dec_int -= 1
    
#example
no=int(input("Enter the number:"))
num=no
sum=0
while no>0:
    sum+=no
    no-=1
print(num)
print(sum) 

#for loop
word="HELLO WORLD"
for letter in word:
    print(letter)
    
user_str = input("Please enter a string.")
count = 0
for char in user_str:
    count += 1
print(user_str)  
print(count)

#range()
one_input=range(5,26,5)
for num in one_input:
    print(num)
    
#range() example
for num in range(1,51):  
    if num%3==0 and num%5==0:
      print("FizzBuzz")
    elif num%3==0:
      print("Fizz")
    elif num%5==0:
      print("Buzz")
    else:
       print(num)'''
       

