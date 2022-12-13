#4.Write a function to add two numbers. Another function to multiply two numbers.
#Get two numbers from user input. If one of the inputs is greater 10, call the addition function.
#If not call the multiplication function with the first number and 3 as input.
#Get the result and call the addtion function with the result and the second input.

number1=int(input("Enter the number1: "))
number2=int(input("Enter the number2: "))
number3=3

#addition function
def addtion(num1,num2):
    add=num1+num2
    return add
    
#multiplication function
def multiply(num1,num2):
    mul=num1*num2
    return mul
 
 
# one of the inputs its greater 10 call the addition function
if(number1>10 or number2>10):
    addresult=addtion(number1,number2)
    print("addtion: ",addresult)
    
else:
    #if not call the multiplication function first number and 3 as input
    mulresult=multiply(number1,3)
    print("multiply: ",mulresult)
    #get the result and call the addtion function result is second number
    addmulresult=addtion(number1,mulresult)
    print("additon: ",addmulresult)
    


