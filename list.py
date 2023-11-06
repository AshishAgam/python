'''print(list("asdf"))

#in and not in keyword in the list
check_list=[1,2,3,4]
print(1 in check_list)

check_list=['a','b','c']
print('a' not in check_list)

mixed = [10, 4.97, True, "mountain", [9, 8, 7]]
print(type(mixed))

li_str = list("cheese")
print("e" in li_str)
print("a" not in li_str)

lst=["Ashish","Kuldeep","Aniket"]
print(lst[1])

index_example=[[1,2,3],[4,5,6],[7,8,9]]
print(index_example[2][1])
print(index_example[2])

mixed = [10, 4.97, True, "mountain", [9, 8, 7]]
print(mixed[1]+2)

#slicing 
lst=[1,2,3,4,5,6,7,8,9]
print(lst[:4])
print(lst[2:7])
print(lst[5:])
print(lst[1:8:2])

#reassigning value
example=[1,2,3,4,56,7,8,99,88,10,]
print(example)
example[3]=12
print(example)
example[0:3]=[10,110,22]
print(example)

#del in list method
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
print(arctic_animals)
#.remove()
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.remove("elephant")
print(arctic_animals)

#.append()
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.append("lion")
print(arctic_animals)


#insert()
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.insert(1,"monkey")
print(arctic_animals)

#.sort()
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.sort()
print(arctic_animals)

#.sort(reverse=True)
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.sort(reverse=True)
print(arctic_animals)

#index()
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
print(arctic_animals.index("elephant"))

#.pop()
arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.pop()
print(arctic_animals)

arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals.pop(3)
print(arctic_animals)'''

#import copy
import copy
abc=[1,2,3,4,5,6]
efg=copy.deepcopy(abc)
efg[2]=4
print(efg)
