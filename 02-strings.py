concatenation = "hello" + " " + "world"
print(concatenation)  # hello world

# String formatting
# %s: string
# %d: numbers (integers)
# %f: numbers (floating point numbers)
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
name = "John"
welcome = "Hello, %s!" % name
print(welcome)  # Hello, John!

age = 23
template = "%s is %d years old"
text = template % (name, age)  # 👈🏻 This parenthesis is a tuple
print(text)  # John is 23 years old

list_as_text = "List: %s" % [1, 2, 3, 4]
print(list_as_text)  # List: [1, 2, 3, 4]

repeat = "spam " * 3
print(repeat)  # spam spam spam

format_float = "Limited decimals: %.2f" % 1.23456789
print(format_float)  # Limited decimals: 1.23

length = len("abc")
print(length)  # 3

position_of_b = "abc".index("b")
print(position_of_b)  # 1

how_many_a = "aabc".count("a")
print(how_many_a)  # 2

# [start:end] "end" index is not captured
only_hello = "Hello world!"[0:5]
print(only_hello)  # Hello


# [start:end:step] "step" avoid to capture chars between jumps
partial_hello = "Hello world!"[0:5:2]
print(partial_hello)  # "Hlo"

# Trick: reverse text with last operation: [::-1]
# Explantion:
# - No start and end will capture entire string.
# - -1 will jump backwards
reverse = "hello"[::-1]
print(reverse)  # "olleh"

upper = "Hello".upper()
print(upper)  # "HELLO"

lower = "Hello".lower()
print(lower)  # "hello"

starts = "Hello world".startswith("Hello")
print(starts)  # True

ends = "Hello world".endswith("world")
print(ends)  # True

words = "Hello world".split(" ")
print(words)  # ["Hello", "world"]
