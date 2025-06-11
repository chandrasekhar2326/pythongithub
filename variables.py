              ## Valid Variables
'''
first_name = "Chandra"
last_name  = "Sekhar"   ## Vaild Variables beacuse variables contain letters,numbers and underscores(_)
print(first_name)
print(last_name)
'''
               ## Invaild Variables 
'''
2firstname =30          In this line Variable name cant be start with numbers
first-name ="chandra"   In this Line variable name doesnt having '-'
print(first-name)
@lastname = "sekhar"    In this line Variable name doesnt having '@'
first@name="krish"
print(first@name)       In this line Variable name doesnt having '@'
'''

               ##Type Conversions
'''       
age =20                 here we assign a value to variable
print(type(age))        here we are checking the type the variable 
age_str = float(age)    here we convert the above variable and assign to new variable 
print(age_str)          printing the variable
print(type(age_str)     checking the type of the variable
'''

               ##Another type of type conversion
'''
age=20                   Here we assign a value to a variable
print(type(age))         here we are checking the type of a variable
print(type(str(age)))    here we converting the age to string
'''
               ##Vaild and Invaild Type Conversions
'''
age ='20'
print(type(age))        Here we convert the number string means numbers inside the strig format will vaild to convert str to int only string inside numbers
print(type(int(age)))
'''
'''
name='Chandra'
print(type(name))       Here We Cant covert the string into interger because we cant convert the string inside leeters conversion to intergers is invaild
print(type(int(name)))
'''
                 ## Assgning Value using Input
''' 
num1 = int(input("Enter the number1"))
num2 = int(input("Enter the number2"))

sum = num1+num2
sub = num1-num2
product = num1*num2
division = num1/num2

print(sum)
print(sub)
print(product)
print(division)
'''