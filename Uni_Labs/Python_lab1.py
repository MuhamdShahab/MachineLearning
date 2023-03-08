def addition():
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    return a+b #return the summation of two number
def subtraction():
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    return a-b #return after subtracting number
def multiplication():
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    return a*b #returns the product
def division():
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    return a/b #return the quotient



inp = "Initial" #value initialized
while((inp != "Quit") and (inp != "quit")):#continues till Quit
    print("Select one of the choice from the list below:\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quit\n")
    inp = str(input())
    if(inp == "Addition"):
        print("Answer: ", addition())
    elif(inp == "Subtraction"):
        print("Answer: ", subtraction())
    elif(inp == "Multiplication"):
        print("Answer: ", multiplication())
    elif(inp == "Division"):
        print("Answer: ", division())
    elif(inp == "Quit"):
        print("Program Finished")
    else:
        print("Not Valid Input.ReType")#exception handled