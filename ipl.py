#Example of List using in if else statement
'''captains=["Rohit Sharma", "M.S. Dhoni", "Virat Kohli", "Hardik Pandya", "Shreyash Iyer", "K.L. Rahul", "Rishab Pant", "Shikhar Dhavan"]
name=input("Enter name of player:")
if name==captains[0]:
    print(""+str(name)+" is captain of Mumbai Indians")
elif name==captains[1]:
    print(""+str(name)+" is captain of CSK")
elif name==captains[2]:
    print(""+str(name)+" is captain of RCB")
elif name==captains[3]:
    print(""+str(name)+" is captain of GT")
elif name==captains[4]:
    print(""+str(name)+" is captain of KKR")
elif name==captains[5]:
    print(""+str(name)+" is captain of LSG")
elif name==captains[6]:
    print(""+str(name)+" is captain of DC")
elif name==captains[7]:
    print(""+str(name)+" is captain of PKXI")
else:
    print("This player is a not captain of any team")
    
a=int(input("select 1 for enter in program or select 0 for exit of program:"))
if a == 1:
    print("Welcome to program")
else:
    print("exit")
captains=["Rohit", "Dhoni", "Virat", "Hardik", "Shreyash"]
name=input("Enter name of player:")
for captain in captains:
    if name=="Virat":
      print("virat is captain of RCB")
      break
    else:
     name=input("Enter name of player:")
a=int(input("select 1 for enter in program or select 0 for exit of program:"))


# prompt

print("welcome to this terminal program")
print("Select from following options")
print("Select -> 1 - continue \nSelect -> 2 - Exit the program")
user_input = int(input())

if user_input == 1:
    print("Enter the caption name:")
    user_selections = input(": ").lower()
    if user_selections == "virat":
        print("Virat is captop of Bangluru team.")
elif user_input == 2:
    print("exiting program")
    exit()

else:
    print("Select -> 1 - continue \nSelect -> 2 - Exit the program")
    user_input = int(input())
    

print("Select -> 1 - continue \nSelect -> 2 - Exit the program")
user_input = int(input())
if user_input==1:
    print("Welcome to Program")
    select=str(input("Enter name of the captain"))
    print(select)
    while select!="virat":
        print("while")
        print(select)
        if select == "virat":
         print("if")
         break
        else:
         input("Enter name of the captain")

        
        
elif user_input==2:
    print("exit program")
    exit()
else:
    print("Select -> 1 - continue \nSelect -> 2 - Exit the program")
    user_input = int(input())'''
    
print("Select from following options")
select=int(input("Select  1 - continue \nSelect  2 - Exit the program"))
if select != 1 or select != 2:
    select=int(input("Select  1 - continue \nSelect  2 - Exit the program"))
elif select==1:
    print("Wel-Come to python program")
    i=True
    while i== True:
        select=str(input("Enter name of the captain:").title())
        if select=="Virat":
            print("virat is a captain of RCB")
            i = False
        
elif select==2:
    print("Exit program")
    exit()

    


