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