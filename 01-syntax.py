# Console output
print("Print statement")

# Conditionals
if 1 == 1:
    print("x is 1")

# Variables
# - Not typed.
# - No need to declare variables before using them.
variable = "content"
print("content")  # content

variable_1, variable_2 = 1, 2
print(variable_1)  # 1
print(variable_2)  # 2

#  Data Types
# Strings
string_double_quotes = "string with double quotes"
string_single_quotes = 'string with single quotes'
print(string_double_quotes)  # string with double quotes
print(string_single_quotes)  # string with single quotes

# Numbers
number = 5
float_number = 5.0
print(number)  # 5 (Integer)
print(float_number)  # 5.0 (float)

float_number = float(5)  # 👈🏻 Another way to create floats.
print(float_number)  # 5.0 (float)

# Lists
# Can contain any type, and without limit.
list = [1, 2]  # 👈🏻 Initialization
list.append(3)  # 👈🏻 Add elements to the list
print(list)  # [1, 2, 3]
