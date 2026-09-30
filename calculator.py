# python program to create a simple calculator

# 3teps to build  calculator program
# 1. funcations for operations
# 2. user input
# 3. print result

# step-1: create function:
# function to add  two numbers
def add(num1,num2):
    return num1+num2

# function to substract  two numbers
def sub(num1,num2):
    return num1-num2

# function to multiply  two numbers
def multiply(num1,num2):
    return num1*num2

# function to divide  two numbers
def divide(num1,num2):
    return num1/num2

# function to multiply two numbers
def avg(num1,num2):
    return (num1+num2)/2

# step-2: user input
print("please select a operation:\n" \
      "1. addition\n"\
        "2. substration\n"\
        "3. multiplication\n"\
        "4. division \n"\
        "5. average\n")

select = int(input("select a operation from 1,2,3,4,5:"))

number1=  int(input("enter first number:"))
number2 =  int(input("enter second number:"))

#step-3: print the result  

if select == 1:
    print(number1, "+",number2, "=",\
          add(number1,number2))

elif select == 2:
    print(number1, "-",number2, "=",\
          sub(number1,number2))

elif select == 3:
    print(number1, "*",number2, "=",\
          multiply(number1,number2))

elif select == 4:
    print(number1, "/",number2, "=",\
          divide(number1,number2))

elif select == 5:
    print("(",number1, "+",number2,")","/","2" "=", \
          avg(number1,number2))
 
else:
    print("invalid operation! pls select again!")
