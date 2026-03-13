# wap to print factorial of given number

num = int(input("Enter any Number for factorial: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i
print(fact)