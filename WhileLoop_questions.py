# Fibonacci using while loop
# n = 10   # how many numbers you want
# a, b = 0, 1
# count = 0

# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b   # update values
#     count += 1

# wap to print table
i = 1
num = int(input("enter any Number: "))
while i <= 10:
    ans = num * i
    print("num x ", i, " = ", ans)
    i = i+1

# wap to print odd numbers

i = 10
while i <= 40:
    if i % 2 != 0:
        print("odd: ", i)
        i = i +1

num = int(input("Enter any Number for factorial: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("Factorial of", num, "is:", fact)
        