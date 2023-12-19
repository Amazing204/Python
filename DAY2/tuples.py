'''
Definition: In Python, a tuple is an ordered, immutable collection of elements. It is created using parentheses ().

Immutability: Tuples are immutable, meaning once created, their elements and length cannot be changed. This ensures data integrity and stability.

Syntax: Elements within a tuple are separated by commas. For example: (1, 'apple', 3.14).
'''

friends = ("krushna" , "rutik" , "sidhartha" , "shubham" ,"rutik")
print(type(filter))
print(friends)

#accessElements
print(friends[1])

#count
print(friends.count("rutik"))
#index
print(friends.index("rutik"))

#we cannot change tuple but there is a jugaad , list bana do , edit kro then , back to tuple

dost = list(friends)
print(dost)
dost.append("mayank")
friends = tuple(dost)

#joining
bhai = ("sahil","sagar","karan")
survival = bhai + friends
print(survival)