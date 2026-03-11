# A Dictionary represents a group of elements in the form of key value pairs
# Dictionary in python is unordered collection
# Dictionary are mutable so we can modify it's items without changing there identity
'''
Dictionary are represented using curly brackets {}

'''
stu = {
    101: 'Ankit', 102: 'Amit', 103: 'Rahul', 103:"Aman"
}
print(stu)

dict_name = {}
print(dict_name)

'''
Key Rules:

*  Key should be unique
*  If we mention same key again, the old key will be overwritten
* key should be immutable integer, string,or tuple
* we cannot use list or dictionaryas key
'''

print(stu[102])

stu.update({105: 'saurabh'})
print(stu)