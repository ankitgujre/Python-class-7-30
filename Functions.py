# Function is a block of code which only runs when it is called.
'''
A function can return data as a result
A function helps avoiding code repetition
'''

def myCollege():
    print("Welcome to my college")

print("Welcome to cybrom")
myCollege()
myCollege()
myCollege()

# return values
'''
function can send data back to the code 
'''

# def myClass():
#     return "I am python student"

# ans = myClass()
# print(ans)

# print(myClass())

''' Python Functions Argumnet '''

# def myName(nm):
#     print("My name is: ", nm)

# myName("ankit")
# myName("amit")
# nm = input("Enter name: ")
# myName(nm)

# Adding two numbers

# def myAdd(no1,no2):
#     ans = no1+no2
#     print("Addition: ", ans)

# myAdd(10,20)
# myAdd(100000,200)

# def myCube(no):
#     ans = no*no*no
#     return ans

# print(myCube(5))

# myCube(6)

'''
default parameter
'''

# def myColg(clg = "Cybrom"):
#     print("My college is = ", clg)

# myColg("Patel")
# myColg()


'''
passing different datatypes
'''

# def myData(nm):
#     for i in nm:
#         print("Miss.",i)

# name = ["sanju","anju", "manju", "ranju"]
# myData(name)


# def myData(data):
#     mans = []
#     for a in data:
#         if a%2 == 0:
#             mans.append(a)
#     print(mans)


# lst = [2,4,6,85,96,4,3,12]
# myData(lst)


# wap to factorial of given number using function 

# def myFacto(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     print(fact)
# # fact = 1
# myFacto(5)

def max(*num):
    max = 0
    for i in num:
        if max < i:
            max = i
    return max

ans = max(45,50,1,6,85,102,180,100)
# num = 45,50,1,6,85,102,180,10
print(type(ans))
print(ans)
# print(max(num))
# a = max(num)
# print(type(a))