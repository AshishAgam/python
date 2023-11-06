'''#tuple
week=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
print(type(week))
print(week)



#for loop using tuple
week=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
for days in week:
    print(days)
print(week[1])
print(len(week))

#while loop using tuple
week=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
count=0
while count<len(week):
    print(week[count])
    count+=1
    
#reverse print using while loop   
week=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
count=len(week)-1
while count>=0:
    print(week[count])
    count-=1
    
#slicing
int=(1,2,3,4,5,6,7,8,9,10)
print(int[1:5])
print(int[-9:-1])
#step slicing
print(int[7::-1])
print(int[8::-2])
print(int[1::3])

#nested tuple
nested=(1,2,3,(4,5,6),(7,8,9),(10,11,12))
print(nested)
print(nested[4])
print(nested[5][1])'''

#count()
repeat=(1,2,3,0,1,2,0,0,3,4,5,6,4,1)
# print(repeat.count(0))
# print(repeat.count(1))
# print(repeat.count(4))
print(repeat.index(0))
print(repeat.index(3))
print(repeat.index(4))