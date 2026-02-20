d = {"yes": "si", "no": "no", "one": "uno", "two": "dos", "tree": "arbol"}

print(dir(d))

#get, tell you if the key is in the dictionary
#(d["carrot"])
print(d.get("carrot", "undefined"))
print(d.get("tree", "undefined"))
#keys and values gives you the list of keys and values
print(list(d.values()))
print(d.keys())
print(d.items())
print(d.pop("yes"))
print(d)
# setdefault is like get, but also sets it if it's not there!
print(d.setdefault("car", "coche"))
print(d.setdefault("car", "automovil"))

