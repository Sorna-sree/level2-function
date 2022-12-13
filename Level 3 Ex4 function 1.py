#Using functions.
#1. Write a function to add two numbers. Get user input (2 numbers) and 
# use the function to add the numbers.
#Print the result from the main code.
#Hint - Funtion will take two input parameters and return one value.

number1=int(input("Enter  number1: "))
number2=int(input("Enter number2: "))
result=0

def add_number(num1,num2):
    result=num1+num2
    return result

result=add_number(number1,number2)
print("add two number is: ",result)