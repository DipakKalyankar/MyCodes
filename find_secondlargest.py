numbers = [12, 35, 1, 10, 34, 35]

largest=numbers[0]
second_largest=None

for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i 
    elif i!=largest:
        if (second_largest is None) or (i>second_largest):
            second_largest=i

if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)
    
#Additional Test Cases:

#Test 1

numbers = [5,5,5,4]

largest=numbers[0]
second_largest=None

for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i 
    elif i!=largest:
        if (second_largest is None) or (i>second_largest):
            second_largest=i

if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)  
 
#Test 2    

numbers = [10,10,10]

largest=numbers[0]
second_largest=None

for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i 
    elif i!=largest:
        if (second_largest is None) or (i>second_largest):
            second_largest=i

if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)
    
#Test 3

numbers = [-5, -2, -10, -1]  

largest=numbers[0]
second_largest=None

for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i 
    elif i!=largest:
        if (second_largest is None) or (i>second_largest):
            second_largest=i

if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)    
                        
    
        
           
       
        
    
