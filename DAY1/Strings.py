myString = "The quick brown fox jumps over a lazy dog."
myString2 ="testing"

length = len(myString)
print("the length of the string is " + str(length))

charAt = myString[2]
print("the character at the particular index " + charAt)

Slice = myString[1:10]
print("the slicing of the string looks like " + Slice)

concat = myString + myString2
print("the this is the concatation of the string " + concat)

repeat = myString2 * 3
print(repeat + " ")

upperCase = myString.upper()
print(upperCase)

Occurance = myString.count("o")
print("the occurance of the letter in the string " + str(Occurance))

position = myString.find("dog")
print("the position is : " + str(position))

replacement = myString.replace("dog","cat")
print(replacement)

