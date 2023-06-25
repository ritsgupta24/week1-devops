# Demo Calculator App For Week 1 Project
# Addition Method
def add(a, b):
    return a + b


# Subtract Method
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b

#Exponential 
def expo(a,b):
    return a ** b 

#Percentage 
def perc(a,b): 
#round off the result to 2 decimal places
    return round(mul(div(a,b), 100),2)
    
def rem(a,b):
#round off the result to 2 decimal places 
    return(a%b)

if __name__ == "__main__":
    # Declare variable and set default values
    a = 4
    b = 2
    print("Sum of " + str(a) + " and " + str(b) + " is ", add(a, b))
    print("Difference of " + str(a) + " and " + str(b) + " is ", sub(a, b))
    print("Product of " + str(a) + " and " + str(b) + " is ", mul(a, b))
    print("Division of " + str(a) + " and " + str(b) + " is ", div(a, b))
    print("Exponential of " + str(a) + " raised to the power of " + str(b) + " is ", expo(a,b))
    print(str(a) + " as a percentage of " + str(b) + " is ", perc(a,b))
    print("Remainder of " + str(a) + " to " + str(b) + " is ", rem(a,b))
