#3. Write a function that returns if a person is a child (age 12 or below),
# Teen (age 13-19),
#adult (20-65) or senior citizen (above 65). (Function should not do anything more than this)
#Get the user's birthyear as input.
#Based on the user's age group, decide what jobs they can do.
#Hint (have a list of jobs for different age groups).


birth_year=int(input("Enter your birthday year"))

#age calculation
age=2022-birth_year
print(age)

#store the age group in a list
Group_list=["child","Teen","Adult","Senior citizen"]

def ageGroup(age,Gruoplist):
    #child (age 12 or below)
    if (age<=12):
        return Group_list[0]
    
    # Teen (age 13-19)
    if(age<=13 and age>=19):
        return Group_list[1]
    
    #adult (20-65)
    if(age>=20 and age<=65):
        return Group_list[2]
 
    #citizen (above 65)
    if(age>65):
        return Group_list[3]
        
    

#function call
Group=ageGroup(age,Group_list)
print("If the person is ",Group)




    