#Tuples

# [1,2,3] --> this one you can modify
# (1,2,3) --> you cannot modify it --> STR

# this is a list ["A", "B", "C"]

#A dictionary is with a curled bracket {}
#A dictionary in Python is a built-in data structure that stores data in key–value pairs,
# where each key is unique and is used to access its corresponding value.

#dictionary example
d = {} #empty dictionnary
print(d)
print(type(d))
d = {"yes": "si", "no": "no", "one": "uno", "two": "dos", "tree": "arbol"}
print(d)
print(type(d))
#indexing
print(d["tree"])
word = input("I speak spanish, give me a word to translate")
print(d[word])

for k in d:
    print(k, d[k])
#same as below!
for k, v in d.items():
    print(k, v)

#i can add more items
d["peacock"] = "pavo real"
print(d)

#i can remove items from the dictionary
del d["one"]
print(d)
d[11] = "once"
print(d)
