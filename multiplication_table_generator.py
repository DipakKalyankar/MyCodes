import time #Importing time library to execute particular execution after some time

time.sleep(1)
print("Multiplication Table Generator!")
time.sleep(1)
n=int(input("Enter your number:")) #Taking number as an input of which Multiplication Table is to be printed

for i in range(1,11): #Loop to print the n number's Multiplication Table 
    print(i*n)        
    
             

    
