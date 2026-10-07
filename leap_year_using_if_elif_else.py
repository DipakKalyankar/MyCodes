Year=int(input("Enter current year:")) #Taking year as a input from user
if Year%400==0: #True condition for a leap year
    print("It's a leap year!")
elif (Year%100==0): #False condition for a leap year
    print("It's not a leap year!")
elif (Year%4==0): #True condition for a leap year 
    print("It's a leap year!")
else: #If above conditions are false then given year is not leap year
    print("It's not a leap year!")
    
