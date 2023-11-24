# i=True
# while i == True:
#   print(i)
#   print(i)
#   print(i)
#   print(i)
#   print(i)
#   print("end")
#   i=False


# print("Select from following options")
# select=int(input("Select  1 - continue \nSelect  2 - Exit the program"))
# if select==1:
#     print("Wel-Come to python program")
#     i=True
#     while i== True:
#         select=str(input("Enter name of the captain:").title())
#         if select=="Virat":
#             print("virat is a captain of RCB")
#             i = False
        
# elif select==2:
#     print("Exit program")
#     exit()
# else:
#     select=int(input("Select  1 - continue \nSelect  2 - Exit the program"))
    

user_input=int(input("select 1 for add value \nselect 2 for remove value \nselect 3 for versatile condition"))
ipl_team={"MI":"Rohit Sharma","CSK":"M.S.Dhoni","RCB":"Virat Kohli","GT":"Hardik Pandya"}
if user_input==1:
#Add element
    print("Wel-come for add element")
    input_key=input(str("Enter key:"))
    input_value=input(str("Enter value:"))
    ipl_team[input_key] = input_value
    print(ipl_team)
#Remove element
elif user_input==2:
    print("Wel-come for remove element")
    delete=input("select removed team:")
    ipl_team.pop(delete.upper())
    print(ipl_team)
#versatile condition
elif user_input==3:
    select_team =str(input("Enter team name or captain name:"))
    for team in ipl_team.keys():
        if team ==  select_team.upper():
            print(ipl_team[team])
            exit()
        
        elif select_team.title() == ipl_team[team]:
            print(team)
            exit()
else:
    print("incorrect number")
    

    





# [
#     1:{"TeamName": "CSK"},
#     2: {},
#     3: {},
#     4: {},
# ]


# ["csk", "mi", "rcb", "csk", "dd"]
