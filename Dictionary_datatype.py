# A Dictionary represents a group of elements in the form of key value pairs
# Dictionary in python is unordered collection
# Dictionary are mutable so we can modify it's items without changing there identity
'''
Dictionary are represented using curly brackets {}

'''
# stu = {
#     101: 'Ankit', 102: 'Amit', 103: 'Rahul', 103:"Aman"
# }
# print(stu)

# dict_name = {}
# print(dict_name)

'''
Key Rules:

*  Key should be unique
*  If we mention same key again, the old key will be overwritten
* key should be immutable integer, string,or tuple
* we cannot use list or dictionaryas key
'''

# print(stu[102])

# stu.update({105: 'saurabh'})
# print(stu)

# we can access the value of a dictionary by reffering to its key name, inside square

# Modifying
# We can Modify the existing value of key by assingning a new alue

# stu[102] = "Python"
# print(stu)

# Adding Dictionary item in python
'''
We can add an item to dictionary just by mentioning new key value pair into an existing dictionary
The new item may be added at any place in the dictionary as dictionary is an unordered collection
'''

# stu[105] = "Rajan"
# print(stu)

# deleting Dictionary item
'''
we can delete an item of dictionary or entire dictionnary using del statement
'''

# del stu[101]
# print(stu)

# test key
# We check whether a key is already exists or not for this purpose we use membersship operator

# print(101 in stu)

# clear() method is used to remove all the items /elements from the dictionary
# stu.clear()

'''
copy() method is used to copy all the elements from the existing dictionay into a new dictionay
'''

# new_dict = stu.copy()
# print(new_dict)

# formkeys() method
'''
It is used to create a new dictionary with the specified keys and values
'''
# key1 = (101,102,103)
# value1 = 'ankit','amit','sumit'

# new_dic = dict.fromkeys(key1, value1)
# print(new_dic)  # {101: ('ankit', 'amit', 'sumit'), 102: ('ankit', 'amit', 'sumit'), 103: ('ankit', 'amit', 'sumit')}

'''
get() method
This method returns the value of the specified key.
If key is not found then it will return none or default value
'''

# a = {1:'A',2:'B'}
# ret = a.get(20, 'Not found')
# print(ret)

'''
items() method
This method returns an object that contains key-value, pairs of dictionary.
The pairs are stored as tuples in the object.
'''
stu = {
    101: "Ankit", 102:"Amit",103:"Sumit"
}

# new = stu.items()
# print(new) # dict_items([(101, 'Ankit'), (102, 'Amit'), (103, 'Sumit')])

'''
keys() method
This method returns a sequence of keys from the dictionary
'''
# new = stu.keys()
# print(new)    # dict_keys([101, 102, 103])

'''
values() method
This method returns a sequence of values from the dictionary
'''
# new = stu.values()
# print(new)   # dict_values(['Ankit', 'Amit', 'Sumit'])

''''
Dictionary update() method
This method is used to update the dictionary with specified key value pair

'''
# stu.update({105: "update"})
# print(stu)

'''
pop() method
This method is removed the item with specified key. 
It returns the removed items value
If key is not found then a default value is returned
'''

# x = stu.pop(105, "not found")
# print(x)
# print(stu)
