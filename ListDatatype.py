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