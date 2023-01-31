def add(start_number, operation_number):
    return start_number + operation_number

def subtract(start_number, operation_number):
    return start_number - operation_number

def multiply(start_number, operation_number):
    return start_number * operation_number

def divide(start_number, operation_number):
    return start_number / operation_number

def index(start_number, operation_number):
    result = start_number
    i = 1
    while i < operation_number:
        result = result * start_number
        i += 1
    return result