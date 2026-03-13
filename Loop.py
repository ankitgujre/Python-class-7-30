# Python Loops
# While Loop
# Python has two primitive loops command while and for loop
i = 1

while i <= 10:
    print(i)
    i = i+1


# Python While Loop is used to execute a block of statements repeatedly until a given condition is 
# satisfied. When the condition becomes false, the line immediately after the loop in the program is 
# executed.

# In this example, the condition for while will be True as long as the counter variable (count) 
# is less than 3. 





# wap to print table
i = 1
num = 5
while i <= 10:
    print(num*i)
    i = i+1


# wap to print factorial
num = int(input("Enter any Number: "))
while num <= 10:
    print(2 * num)
    num = num + 1
# wap to print odd number between 10 to 40

i = 10
while i <= 40:
    if i % 2 != 0:
        print("Odd:", i)
    i = i + 1

# wap to print factorial

num = int(input("Enter any Number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("Factorial of", num, "is:", fact)