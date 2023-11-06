#dictionaries
'''dic={"a":1, "b":2, "c":3, "d":4}
print(dic)
print(dic["c"])
print("a" in dic)
print("f" not in dic)

#dictionaries methods
#keys()
dict={"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", 
 "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
print(dict.keys())
for keys in dict.keys():
    print(keys)
    
#values()
print(dict.values())
for values in dict.values():
    print(values)
    
#items()
print(dict.items())
for item in dict.items():
    print(item)
    
#get()
if "Queen" in dict:
    print(dict["Queen"])
else:
    print("Not found in dictionari")
print(dict.get("ashish", "Not found in dictionari"))

#len()
print(len(dict))

#.fromkeys()
for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)

ex={}.fromkeys("[asdf]", "consonant")
print(ex)

#pop()
birth_year={1999:"Aniket", 2000:"Vaibhav", 2002:"Ashish", 2003:"Kuldeep"}
popped=birth_year.pop(2002)
print(birth_year)
print(popped)

#popitem()
birth_year={1999:"Aniket", 2000:"Vaibhav", 2002:"Ashish", 2003:"Kuldeep"}
popped=birth_year.popitem()
print(birth_year)
print(popped)

#update()
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)

copy=internet_celebrities.copy()
print(copy)

internet_celebrities.clear()
print(internet_celebrities)

#setdefault()
dict={1:1, 2:4, 3:9, 4:16}
print(dict)
dict.setdefault(5,25)
print(dict)'''

#dict()
empty=dict()
print(empty)

with_value=dict(a=1,b=2,c=3)
print(with_value)
