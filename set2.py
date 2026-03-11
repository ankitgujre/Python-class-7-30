"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are 
List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)  # duplicate items not allowed


'''
Add sets
To add items from another set into the current set, use the update() method.
'''

Myset = {"raju", "sanju", "anju"}
youset = {"rajesh", "mahesh"}
print(Myset)
Myset.update(youset)
print(Myset)
print(sorted(Myset))

# Add any iterable
# The object in the update() method not have to be a set, it can be any iterable object (tuple,list,dictionaries)

s2 = {1,2,3}
naam = ["Ankit", "amit","sumit"]
naam2 = {"Suman","raman", "naman"}
s2.update(naam)
print(s2)

'''
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are 
List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
'''

thisIsSet = {"Apple", "Mango","Banana"}
print(thisIsSet)
# Note: Set items are unordered, so you cannot be sure in which order the items will appear.
set2 = {"Apple", "Mango","Banana"}
print(set2)

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)