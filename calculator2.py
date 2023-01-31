import sys
from calc import add, subtract, multiply, divide, index

def conversions(operation,start_number,operation_number):
    operation = operation.lower()
    start_number=float(start_number)
    operation_number=float(operation_number)
    calculation(operation,start_number,operation_number)


def calculation(operation,start_number,operation_number):
    if operation == "add":
        result = add(start_number, operation_number)
    elif operation == "subtract":
        result = subtract(start_number, operation_number)
    elif operation == "multiply":
        result = multiply(start_number, operation_number)
    elif operation == "divide":
        result = divide(start_number, operation_number)
    elif operation == "index":
        result = index(start_number, operation_number)
    else:
        raise Exception(f"Unsupported or invalid operation '{operation}'")
    print('Answer: ', result)
    return 0


def main():
    print ("")
    print ("Welcome to the calculator interface v0.2")
    print ("Enter the function you require, followed be the two numbers")
    print ("")
    print ("Available options: ", availableoperation)
    operation = input('Action: ')
    start_number = input('Number 1: ')
    operation_number = input('Number 2: ')
    print ("")
    print ("Sum: ", start_number, operation.upper(), operation_number)
    conversions(operation,start_number,operation_number)

availableoperation = ['Add', 'Subtract', 'Multiply', 'Divide', 'Index']

if __name__ == '__main__':
    sys.exit(main())