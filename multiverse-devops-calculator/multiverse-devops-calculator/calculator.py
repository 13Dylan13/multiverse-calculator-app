import sys
from helpers import add_prefix
from calc import add, subtract, multiply, divide, index

def get_args():
    try:
        return (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
        print("Not all arguments have been provided!")
        print("USAGE: [operation] [start_number] [operation_number]\n")
        raise IndexError
    except:
        print("Unknown error! See the details below.\n")
        raise


def main():
    operation, start_number, operation_number = get_args()
    print(operation)
    print(start_number)
    print(operation_number)

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
    
    print(result)

    return 0


if __name__ == '__main__':
    sys.exit(main())
