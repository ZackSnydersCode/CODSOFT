import re

def add(num1, num2):
    result = num1 + num2
    print(f"Result of addition: {result}")

def sub(num1, num2):
    result = num1 - num2
    print(f"Result of subtraction: {result}")

def mult(num1, num2):
    result = num1 * num2
    print(f"Result of multiplication: {result}")

def div(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"Result of division: {result}")

while True:
    key = input('Enter 0 for custom Calculator or Enter 1 for general Calculator: ')

    if key == '1':
        num1 = float(input("Enter First operand: "))
        op = input("Enter Operator (+, -, *, /): ")
        num2 = float(input("Enter Second operand: "))

        if op == '+':
            add(num1, num2)
        elif op == '-':
            sub(num1, num2)
        elif op == '*':
            mult(num1, num2)
        elif op == '/':
            div(num1, num2)
        else:
            print("Invalid operator")
    elif key == '0':
        print("*******Custom Command********:\nFor addition use add(operand1, operand2)\nFor subtraction use sub(operand1, operand2)\nFor multiplication use mult(operand1, operand2)\nFor division use div(operand1, operand2)\n")
        user_input = input("Enter a custom command: ")
        
        if user_input != 'exit()':
            pattern = r'(\w+)\(([^,]+),([^)]+)\)'
            match = re.match(pattern, user_input)
            
            if match:
                command = match.group(1).strip()
                num1 = float(match.group(2).strip())
                num2 = float(match.group(3).strip())
                
                if command == 'add':
                    add(num1,num2)
                elif command == 'sub':
                    sub(num1,num2)
                elif command == 'mult':
                    mult(num1,num2)
                elif command == 'div':
                    div(num1,num2)
                else:
                    print("Invalid custom command")
            else:
                print("Invalid custom command")
        else:
            break
    else:
        print("Invalid choice. Please enter '0' or '1'.")
