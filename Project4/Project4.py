'''
Project 4: Real Calculator
'''
#function defination
def add(num1, num2):
    print(f"The sum of {num1} and {num2} is {int(num1) + int(num2)}")

def sub(num1, num2):
    print(f"The difference of {num1} and {num2} is {int(num1) - int(num2)}")

def mul(num1, num2):
    print(f"The product of {num1} and {num2} is {int(num1) * int(num2)}")

def div(num1, num2):
    print(f"The result of {num1} divided by {num2} is {int(num1) / int(num2)}")

def quo(num1, num2):
    print(f"The quotient of {num1} divided by {num2} is {int(num1) // int(num2)}")

def rem(num1, num2):
    print(f"The remainder of {num1} divided by {num2} is {int(num1) % int(num2)}")

#printing info
print("Actions that can be performed:\n\nAddition\t --> +\nSubtraction\t --> -\nMultiplication\t --> *\nDivision\t --> /\nFinding only quotient --> //\nFinding only remainder--> % ")
print("\nSample Equation: 12 + 180")
print(" ")

#Accepting the input
num1, operator, num2 = map(str, input("Enter your equation: ").split(" "))

#Conditional switching
if operator == "+":
    add(num1, num2)

elif operator == "-":
    sub(num1, num2)

elif operator == "*":
    mul(num1, num2)

elif operator == "/":
    div(num1, num2)

elif operator == "//":
    quo(num1, num2)

elif operator == "%":
    rem(num1, num2)

else:
    print("Invalid input! Please refer the list of actions and sample equation")


