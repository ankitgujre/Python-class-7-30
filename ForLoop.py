city = ["Bhopal", "Indore", "Jabalpur", "gwalior"]

# for a in city:
#     if a == "Jabalpur":
#         break
#     print(a)

# for a in city:
#     if a == "Jabalpur":
#         continue
#     print(a)

# num = [23,555,588,66,3,5]

# for i in num:
#     if i % 2 == 0:
#         continue
#     print(i)


# Range 
'''
The range() function
To loop through a set of code a specified number of times, we can use the range() function
The range() function returns a sequence of number
'''

# for x in range(6):
#     print(x)

# for c in range(3, 11):
#     print(c)

# for c in range(20, 31):
#     print(c)

# for c in range(1, 21):
#     if c % 2 != 0:
#         print("odd",c)

# for i in range(2, 21, 2):
#     print(i)

# wap to print 5 10 15 upto 50

# for i in range(5, 51, 5):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)
# else:
#     print("Loop is finished")

for i in range(1, 11, 2):
    if i == 7:
        break
    print(i)
else:
    print("Loop is finished")