# wap to print factorial of given number

# num = int(input("Enter any Number for factorial: "))
# fact = 1

# for i in range(1, num+1):
#     fact = fact * i
# print(fact)

'''
wap to count positive numbers
'''

# num = [-1,2,9,-5,3,-90]
# p_count = 0
# for i in num:
#     if i > 0:
#         p_count += 1
# print("Positive = ", p_count)

'''
wap to calculate sum of even numbers upto a given numbers n
'''

# num = [1,2,3,4,5,6,7,8,9,10]
# sum_even = 0

# for i in num:
#     if i % 2 == 0:
#         sum_even += i

# print("Sum of even numbers : ", sum_even)

'''
wap to print numbers from 1 to 10
'''

# for i in range(1, 11):
#     print(i)

'''
wap to print even numbers from 1 to 20
'''

# for i in range(1,21):
#     if i%2 == 0:
#         print("even = ", i)

'''
wap to print table of 5
'''

# for i in range(1,11):
#     # print(5*i)
#     print("5 *",i, " = ", 5*i)

'''
wap to count character in cybrom
'''

# ch = "Cybrom"
# count = 0

# for i in ch:
#     count += 1
# print(count)

'''
wap to print number in reverse order 10 to 1
'''

for i in range(10, 0,-1):
    print(i)


'''
wap to print  umbers in reverse order
'''
num = [1,2,3,4,5,6]

for i in num:
    rev = num[::-1]

print(rev)