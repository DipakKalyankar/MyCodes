import time #Importing time library to run code's particular executions after some time

time.sleep(1)
print("Age verify for voting eligibility!")
time.sleep(2)

Age=int(input("Enter your age:")) #Taking age as a input from user to check voting eligibility 

if Age>=18: #True condition for voting
    print("You are eligible to vote!")
else: #False condition for voting
    print("Sorry! You are not eligible to vote!")    
