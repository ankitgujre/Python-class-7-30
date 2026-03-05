# Change item
'''
Once a set is created you cannot change its item but you can add new items.

Python add set item
to add one item to a set use the add() method
'''
s = {1,2,3}
n = {"raju", "sanju", "anju"}
s.add(50)
print(s)

n.add("ranju")
print(n)

'''
Add sets
To add items from another set into the current set, use the update() method.
'''

Myset = {"raju", "sanju", "anju"}
youset = {"rajesh", "mahesh"}
print(Myset)
Myset.update(youset)
print(Myset)

# Add any iterable
# The object in the update() method not have to be a set, it can be any iterable object (tuple,list,dictionaries)

s2 = {1,2,3}
naam = ["Ankit", "amit","sumit"]
naam2 = {"Suman","raman", "naman"}
s2.update(naam)
print(s2)

'''
Remove set items
To remove an item in a set use the remove(), or the discard() method
'''

# s2.remove(5) # generating error
# print(s2)

# naam.discard("ravi")
# print(naam)

'''
if the item to remove does not exit remove() will raise an error.
if the item to remove does not exit, discard() will not raise an error.

you can also use the pop() method to remove an item but this method will remove a random item
so you cannot be sure what item that gets removed
'''
print(naam2)
myval = naam2.pop()
print(myval)

# clear() method empties the set

print(naam.clear())

# del keyword will delete the set completely

# del s

# print(s)

'''
Python join two set
There are several ways to join two or more sets in python

You can use the union() method that returns a new set containing all items from both sets, or the update() method that insert all the items from one set into another  

The union method returns a new set with all items fro both set
'''
a = {"abc","def","ghi"}
n = {"raju", "sanju", "anju","abc"}
# theset = n.union(a)
# print(theset)

'''
Keep only the duplicate
the intersection_update() method will keep only  the items that are present in both sets.
'''
# theset = n.intersection_update(a)
# print(theset)

# a = {"abc","def","ghi"}
# n = {"raju", "sanju", "anju","abc"}

# n.intersection_update(a)   # n modify ho jayega
# print(n)

# The intersection() method will return a new set, that only contains the items that are present in both set

a = {"abc","def","ghi"}
n = {"raju", "sanju", "anju","abc"}

theset = n.intersection(a)
print(theset)

x = {"apple","banana","cherry"}
y = {"googl", "ms", "apple"}

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print(type(thisset))
print(sorted(thisset))