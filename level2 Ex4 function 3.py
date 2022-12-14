#3. Write a function that returns if a person is a child (age 12 or below),
# Teen (age 13-19),
#adult (20-65) or senior citizen (above 65). (Function should not do anything more than this)
#Get the user's birthyear as input.
#Based on the user's age group, decide what jobs they can do.
#Hint (have a list of jobs for different age groups).


birth_year=int(input("Enter your birthday year"))
#child=["baby","LKG","1 to 5th std"]
#Teen=["Higher secondary school"]
#Adult=["college","teachers","IT employee"]


#age calculation
age=2022-birth_year
print(age)

def child(age):
    if(age<=3):
        print(f" if the person is a baby ")
    if(age>3 and age<=5):
        print(" if the person is a LKG student")
    if(age>5 and age<=12):
        print(" if the person is 1st std to 5th std school student")
        
def Teen(age):
    if(age>=19):
        print(" if the person is Higher secondary school student")

def Adult(age):
    if(age>=20 and age<24):
        print("if the person is college student")
    if(age>=24):
        print("if the person is Teacher")

def senior_citizen(age):
    print(" if the person is Senior Citizen")

#child (age 12 or below)
if (age<=12):
    child_job=child(age)
    
# Teen (age 13-19)
if(age<=13 and age>=19):
    Teen_job=Teen(age)
    
#adult (20-65)
if(age>=20 and age<=60):
    Adult_job=Adult(age)
    
#citizen (above 65)
if(age>60):
    senior_citizen(age)