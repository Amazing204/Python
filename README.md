# Python
Welcome to my Python Learning Repository!


DATA TYPES:
In Python, data types represent the type or category of values that variables can hold. Python is dynamically typed, meaning you don't need to explicitly declare the data type of a variable; the interpreter determines it at runtime.

Integers (int):

Whole numbers without a decimal point.
Example: x = 5
Floats (float):

Numbers with a decimal point or in exponential form.
Example: y = 3.14
Strings (str):

Ordered sequence of characters enclosed in single or double quotes.
Example: name = 'John'
Booleans (bool):

Represents either True or False.
Used for logical operations and conditions.
Example: is_valid = True
Lists (list):

Ordered and mutable collection of items.
Items can be of different data types.
Example: numbers = [1, 2, 3]
Tuples (tuple):

Ordered and immutable collection of items.
Similar to lists but cannot be modified once created.
Example: coordinates = (4, 5)
Dictionaries (dict):

Unordered collection of key-value pairs.
Example: person = {'name': 'Alice', 'age': 30}
Sets (set):

Unordered collection of unique items.
Example: unique_numbers = {1, 2, 3, 4}



TYPE CONVERSION:
You can convert from one type to another with the int(), float(), and complex() methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

NOTE:You cannot convert complex numbers into another number type.   

