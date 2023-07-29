print(2 == 2)  # equal -> True
print(2 == "2")  # equal but type mismatch -> False
print(2 > 1)  # Greater then -> True
print(2 < 1)  # Lesser than -> False

print(2 > 1 and 2 == 2)  # Combined conditions, all must be true -> True
print(2 > 1 and 2 != 2)  # Combined conditions, all must be true -> False
print(2 > 1 or 2 != 2)  # Combined conditions, any must be true -> True

first_list = [1, 2, 3]
second_list = [1, 2, 3]
print(first_list == second_list)  # If list has the same content -> True
print(first_list is second_list)  # If list is the same -> False

negated = not True
print(negated)  # False

count = 0
while count < 5:
    print(count)  # 0, 1, 2, 3, 4
    count += 1

count = 0
while True:  # Infinite loop
    print(count)  # 0, 1, 2, 3, 4
    count += 1
    if count >= 5:
        break  # Will stop the while here

for x in range(10):
    if x % 2 == 0:
        continue  # Will skip if number is even
    print(x)  # 1, 3, 5, 7, 9

count = 0
while count < 5:
    print(count)  # 0, 1, 2, 3, 4
    count += 1
else:
    print("Will be shown because while condition fails")

count = 0
while True:  # Infinite loop
    print(count)  # 0, 1, 2, 3, 4
    count += 1
    if count >= 5:
        break  # Will stop the while here
else:
    print("Will not be shown break was used")
