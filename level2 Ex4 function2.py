#2. Write a function that returns if a food is a healthy food or not. 
#Funtion will take one food item as input. It will return True or false.
# It will have a list of healthy foods. Name the function appropriately.
#From the main code, ask the user about his/her breakfast. 
#Print if it is a healthy breakfast or not.

#it is healthy food list
healthyFood_list=["dosai","idly","pongal","rice","chappathi","sundal"]

#find the breakfast food is healthy food or not
def healthyFood_or_not(breakfast):
    if breakfast in healthyFood_list:
        return True
  
      
breakfast=input("what do you like breakfast: ")
healthyFood=healthyFood_or_not(breakfast)
if(healthyFood==True):
    print("It is a healthy breakfast")
else:
    print("It is not a healthy breakfast")