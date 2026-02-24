# List items are ordered,changeable, and allow duplicate values
name = ["ankit", "raju", "manoj","Ankit","Harsh", "Vikash", "Ramesh"]
print(name)
print(name[3])

# List Length
# To determine how many items a list has, use the len() function.
# List item can be of any data type.
print(len(name))

a = [123, "anuj", True, "raj", 3.14]
print(type(a))

print(a[1])

sub = list(("php", "java", "python"))
print(sub)
print(type(sub))

# list() constructor it is also possible to use the list() constructor when creating a new list. 

# list access item "List item are indexed you can access them by reffering to the index number".

# Negative indexing
# its means start from the end -1 refers to the last -2 refers to the second last item etc.

print(name[-1])
print(name[-3])
print(name[-5])

#Range of indexes
# you can specify a range of indexes by specifying where to start and where to end the range when specifying a range, 
# the return value will be a new list with the specified items.

print(name[2:5])
print(name[5:7])

# By leaving out the start value the range will start at the first item
print(name[:5])

# By leaving out the end value the range will go on to the end of the list

print(name[2:])
print(name[0:])
print(name[:])

# Python Change List item

# To change the value of a specific item refer to the index number

print(name)
name[2] = "Ramesh"
print(name)

# Change a range of item values
# To change the value items within a specific range, define a list with the new values and
# refer to the range of index numbers where you want to insert the new values.

print(name)
name[2:5] = ["bittu", "harshita","Gaurav"]
print(name)

# If you insert more items than you replace

#Append()
# To add an item to the end of the list use the append() method

name.append("mayur")
print(name)

# insert items
# To insert a list item at a specified index, use the insert() method.
# The insert method items an items at the specified index.

name = ["sonu", "sanjay", "sandeep"]
name.insert(1, "sameer")
print(name)

'''
Extend list
To append elements from another list to the current lis, use the extend() method.

'''

name1 = ["manish", "sanju", "rupal"]
name.extend(name1)
print(name)

'''
The extend() method does not have to append list. you can add any iterable object(tuples, set, dictionaries etc.)

'''

name1 = ("manish", "sanju", "rupal")
name.extend(name1)
print(name)

name[8] = "Ankit"
print(name)

'''
Remove List item
The remove() method removes the specified item
'''
name1 = ["manish", "sanju", "rupal"]
name1.remove("sanju")
print(name)

'''
The pop() method removes the specified index.
'''

name.pop(2)
print(name)

'''
the del key word also removes the specified index
'''
# The del keyword can also delete the list completely

thislist = ["apple", "Banana", "Papaya"]
del thislist[1]
print(thislist)

# clear() method empties the list
# the list still remains but it has no contents

thislist.clear()
print(thislist)

'''
Sort list
Sort list alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending by default
'''
thislist = ["Apple", "Banana", "Papaya"]
thislist.sort()  # ascii value ke according sort hogi
print(thislist)
thislist.sort(reverse=True) # to sort descending use the keyword argument reverse = True
print(thislist)

# Revers method
'''
The reverse() method reverses the current sorting order of the elements.
'''
thislist.reverse()
print(thislist)

# copy a list
'''
There are ways to make a copy one way is to use the built-in list method copy()
make a copy of a list with the copy() method:

'''

a = ["sonu", "amit", "rahul"]
b = ["su", "amt", "ra"]

myname = a.copy()
print(myname)

'''
Another way to make a copy is to use the built-in method list()
myname = list(name)
'''