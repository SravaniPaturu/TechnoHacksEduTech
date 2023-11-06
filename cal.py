#program for calculator

#Function to add two numbers
def add(num1,num2):
    return num1+num2

#Function to subtract two numbers
def sub(num1,num2):
    return num1-num2

#Function to multiply two numbers
def mul(num1,num2):
    return num1*num2

#Function to divide two numbers
def div(num1,num2):
    return num1/num2

#Function of modulus of two numbers
def mod(num1,num2):
    return num1%num2

print("Enter your choice:\n","1.Addition:\n","2.Subtraction:\n","3.Multiplication:\n","4.Division:\n","5.Modulus:")

#Select input from user
num1=int(input("Enter First number:"))
num2=int(input("Enter Second number:"))
choice=int(input("Enter choice to perform operation 1,2,3,4,5:"))

if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif choice==2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif choice==3:
    print(num1,"*",num2,"=",mul(num1,num2))

elif choice==4:
    print(num1,"/",num2,"=",div(num1,num2))

elif choice==5:
    print(num1,"%",num2,"=",mod(num1,num2))

else:
    print("Default choice")


