dictionary = {
    "First": 1
}

dictionary["Second"] = 2
dictionary["Third"] = 3
dictionary["Fourth"] = 4

print(dictionary)  # {'First': 1, 'Second': 2, 'Third': 3, 'Fourth': 4}

print(dictionary["First"])  # 1

for key, value in dictionary.items():
    print("Value of key %s -> %d" % (key, value))
    # Value of key First -> 1
    # Value of key Second -> 2
    # Value of key Third -> 3
    # Value of key Fourth -> 4

del dictionary["First"]

print(dictionary)  # {'Second': 2, 'Third': 3, 'Fourth': 4}

dictionary.pop("Second")

print(dictionary)  # {'Third': 3, 'Fourth': 4}
