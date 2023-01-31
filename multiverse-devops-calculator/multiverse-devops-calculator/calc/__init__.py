def add(start_number, operation_number):
    return start_number + operation_number


def subtract(start_number, operation_number):
    return start_number - operation_number


def multiply(start_number, operation_number):
    return start_number * operation_number


def divide(start_number, operation_number):
    return start_number / operation_number


def alt_index(start_number, operation_number):
    result = start_number

    for i in range(operation_number-1):
        result *= start_number

    return result


def index(start_number, operation_number):
    return start_number**operation_number
