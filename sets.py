'''#set
set_1={1,2,3,3,44,5,1}
print(set_1)
set_2=set(["a","b","c","d","e","f"])
print(type(set_2))
print(set_2)
print(len(set_1))

#range
set_3=set(range(1,12,3))
print(set_3)

for num in set_3:
    print(num)
    
#set methods
#add()
set={"a","b","c","d"}
set.add("e")
print(set)
#remove
set.remove("a")
print(set)
#discard()
set.discard("d")
print(set)
#clear()
set.clear()
print(set)
#copy()
set1=set.copy()
print(set1)'''

set_1={1,2,3,4,5,11}
set_2={11,12,13,1,2,3}
#.union() or |
set_3=set_1 |(set_2)
print(set_3)
#.intersection() or &
set_3=set_1 &(set_2)
print(set_3)
#.difference or -
set_3=set_1 .difference(set_2)
print(set_3)
set_3=set_2 -(set_1)
print(set_3)
