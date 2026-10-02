'''
score =int(input("Enter your score: "))
if score >= 100 :
    print("input a valid value")
elif score >= 90 : 
    print("You got an A!") 
elif score >= 80 :
    print("You got a B!")  
elif score >= 70 : 
    print("You got a C!")  
elif score >= 60 :       
    print("You got a D!")  
else:
    print("You got an F!")   
'''

age = int(input("Enter your age: "))
plan = input("Enter your plan (basic, standard, premium): ")
'''
if age < 18:
    print("You are not eligible for any plan.")
else:
    if plan == "basic":
        print("You are eligible for the basic plan.")       
    elif plan == "standard":
        print("You are eligible for the standard plan.")
    elif plan == "premium":
        print("You are eligible for the premium plan.") 
''' 
#trinary operator
result = "You are not eligible for any plan." if age < 18 else "You are eligible for the " + plan + " plan."



