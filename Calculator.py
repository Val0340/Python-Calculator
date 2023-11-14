def add(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def division(num1, num2):
    return ( num1 / num2)

def multiplication (num1, num2):
    return (num1 * num2)


Selection = int(input("Select from operations\n 1.Addtion\n 2.Subtraction\n 3. Division\n 4.Multiplication  : "))

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if Selection == 1:
    print ( num1, "+" ,num2 , "=" , add(num1,num2))
elif Selection == 2:
    print (num1, "-", num2, "=", subtract(num1,num2))
elif Selection == 3:
    print(num1,"/",num2,"=", division(num1,num2))
elif Selection == 4:
    print(num1, "*", num2, "=", multiplication(num1,num2))
else:
    print("Invalid input")