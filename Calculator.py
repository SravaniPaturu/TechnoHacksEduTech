#Program for calculator

#Function to add two numbers
def add(number_1,number_2):
    return number_1+number_2

#Function to subtract two numbers
def sub(number_1,number_2):
    return number_1-number_2

#Function to multiply two numbers
def mul(number_1,number_2):
    return number_1*number_2

#Function to divide two numbers
def div(number_1,number_2):
    return number_1/number_2

#Function of modulus two numbers
def mod(number_1,number_2):
    return number_1%number_2

print("Enter your choice:\n","1.Addition:\n","2.Subtraction:\n","3.Multiplication:\n","4.Division:\n","5.Modulus:")

#select input from user
number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))
choice=int(input("Enter choice to perform operation 1,2,3,4,5:"))

if choice==1:
    print(number_1,"+",number_2,"=",add(number_1,number_2))

elif choice==2:
    print(number_1,"-",number_2,"=",sub(number_1,number_2))

elif choice==3:
    print(number_1,"*",number_2,"=",mul(number_1,number_2))

elif choice==4:
    print(number_1,"/",number_2,"=",div(number_1,number_2))

elif choice==5:
    print(number_1,"%",number_2,"=",mod(number_1,number_2))
    
else:
    print("Default choice")
