a = 300
b = 200

# Shot hand if
if a>b: print("A is greater than B")

print(a) if a>b else print("B")

# nested if shot hand

city = "Bhopal"
age = 21
fees = 50000

if city == "Bhopal":
    if age >= 18:
        print("you can join our class")
    else:
        print("You are from bhopal but you are in under age")
else:
    print("You are not fromm bhopal")

# input 

post = input("Enter post namme: ")
salary = float(input("Enter salry: "))

if post == "Admin":
    if salary > 50000:
        print(salary * 25/100)
    else: 
        print(salary * 15/100)
elif post == "Hr":
    if salary > 50000:
        print(salary * 15/100)
    else: 
        print(salary * 10/100)
    
else: 
    print("Invalid post")