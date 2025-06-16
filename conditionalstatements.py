'''
age =30
if age>=18:                                # IF Statement
    print("You are eligible for voter id")
'''
'''
number =int(input("Enter the number"))
if number>=18:                               # IFELSE Statements
    print("You are eligible for voterid")
else:
    print("You are not eligible for voterid")
'''
'''
number =int(input("Enter the number"))
if number>0:
    print("The number is positive number")
    if number%2==0:
        print("The numeber is the even number number")
'''
'''
 age =19
if age<=12:
    print("you are the child")
      elif age<=18:                                    # IF ELIF Statements
    print("Your are teenager")
 else:
    print("you are adult")
'''
'''
number=int(input("Enter the number:"))
if number>0:
    print("the number is positive")
    if number%2==0:
        print("the number is divisible by 2")     #Nested if Condition
    else:
        print("the number is Odd")
else:
    print("The number is neagtive")
'''
'''
#Determine to write the code for whether the year is leap year or not:

num = int(input("Enter the year: "))

if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
'''
'''
#Determine to write the code for python code for a simple calculator

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operand = input("Enter the operand (+, -, *, /, %): ")

if operand == '+':
    result = number1 + number2
elif operand == '-':
    result = number1 - number2
elif operand == '*':
    result = number1 * number2
elif operand == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        print("Error! Division by zero is not allowed.")
        result = None
elif operand == '%':
    if number2 != 0:
        result = number1 % number2
    else:
        print("Error! Modulo by zero is not allowed.")
        result = None
else:
    print("Invalid operand")
    result = None

if result is not None:
    print("Result:", result)
'''
'''
# Determine the code for price of ticket based on the age and student status

age = int(input("Enter the age: "))
is_student = input("Are you a student? (yes/no): ").lower()
is_oldage = input("Are you a senior citizen? (yes/no): ").lower()

if age < 5:
    price = "Free"
elif age <= 12:
    price = "10rs"
elif age <= 17:
    if is_student == 'yes':
        price = "12rs"
    else:
        price = "15rs"
elif age >= 60:
    if is_oldage == 'yes':
        price = "16rs"
    else:
        price = "20rs"
else:
    price = "25rs"  # For adults (18–59) not covered in previous conditions

print("Price:", price)
'''
'''
    
