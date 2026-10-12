score = 50

def update():
    global score
    print(score)
    score = score + 10

update()
print(score)

#1)Why does the original code raise an error? 
#-->Because Python treats score as a local variable when it is assigned inside the function, so using it before assigning a value causes an UnboundLocalError.
#2)Why use global?
#-->To modify the global variable inside the function.
#3)Corrected output? 
#-->50 and 60.
