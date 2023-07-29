# Iterate a list
list = [1, 2]  # 👈🏻 Initialization
list.append(3)  # 👈🏻 Add elements to the list
list.append(4)
list.append(5)

for item in list:
    print(item)  # 1, 2, 3, 4, 5

concatenation = [1, 2, 3] + [4, 5, 6]
print(concatenation)  # [1, 2, 3, 4, 5, 6]

repeat = [1, 2, 3] * 3
print(repeat)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(1 in [1, 2, 3])  # Find in list -> True

# Iterate by N times (starting by 0)
for number in range(5):
    print(number)  # 0, 1, 2, 3, 4

# Iterate by N times with steps
for number in range(0, 5, 2):
    print(number)  # 0, 2, 4
