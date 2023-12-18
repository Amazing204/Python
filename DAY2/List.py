"""
LIST In Python

-Lists are used to store multiple items in a single variable.

-Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

-List items are ordered, changeable, and allow duplicate values.
Note: There are some list methods that will change the order, but in general: the order of the items will not change.

-A list can contain different data types

-Lists are created using square brackets:
EXAMPLE:
thislist = ["apple", "banana", "cherry" , 1 , 2 , 3 , 3 ,"tarun"]
print(thislist)

"""
myList = ["tarun" , "sahil" , 33 ,54 , True , 1.1]

print(myList)

#LENGTH of the list is functtion len

print(len(myList))

#TYPE 

print(type(myList))


#ACCESS Items

print(myList[2])
print(myList[4])

#Negative Indexing
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.

print(myList[-2])

#Range of Indexes
print(myList[1:4])
print(myList[:4]) #start from first
print(myList[1:]) #goes till the end

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Append Items
#To add an item to the end of the list, use the append() method:
myList.append("lastelement")
print(myList)


#Extend List
#To append elements from another list to the current list, use the extend() method.
tarun = [10,4,8]
sahil = [4,5,6]
tarun.extend(sahil)
print(tarun)
print(sahil)

#copy 
copyMyList = myList.copy()
print(copyMyList)
#or
copyMyList2 = myList[:]
print(copyMyList2)


#sorting
tarun.sort()
print(tarun)
#reverse
tarun.reverse()
print(tarun)


#SEARCHING AND COUNTING
number = [ 1,1,1,1,1,1,22,33,4,5,4,3,3,4,6,7,7,1 ]
print(number)
print(number.index(22)) #return index
print(number.count(1)) #total occurance

#reMOVE and Pop
#list.remove(value) 
#list.pop(index)

number.remove(22)
print(number)
print(number.pop(6))



