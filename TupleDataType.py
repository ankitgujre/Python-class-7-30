# Tuple is used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable. Tuple are written with (parenthesis) or Round Brackets
name = ("ranu", "sanju", "mohan","ajay", "deepak","ankit")
print(type(name))
print(name)
# Tuple length: To determine how many items a tuple has, use the len() function.

print(len(name))

print(name[:3])

# single item ka tuple nahi banta string kehlata hai ("ankit")
# To create a tuple with one item, you have to add a comma after the item, otherwise python will
# not recognize it as a tuple
myname = ("Ankit",)
print(myname)

# A tuple can contain different data types

tup = (12,11,"ankit",'a',3.14, True)
print(tup)

# The tuple() constructor
# it is also possible to use the tuple() constructor to make a tuple
mynm = tuple(["ankit","amit","sandeep"])
print(mynm)
mynm = tuple(("ankit","amit","sandeep"))
print(mynm)

# Negative indexing
# Negative indexing means starts from the end, -1 refers to the last item.

print(name[-1])

# Range of indexes
# you can specify of indexes by specifying where to start and where to end the range.
# when specifying a range the return value will be a new tuple with the specified items.

name = ("ranu", "sanju", "mohan","ajay", "deepak","ankit")

print(name[2:5])

# By leaving out the start value, the range will start at the first item

print(name[:4])

# By leaving out the end value, the range will go on the end of the tuple.

print(name[2:])

