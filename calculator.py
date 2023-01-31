import sys
from calc import add, subtract, multiply, divide


def get_args():
    try:
        return (sys.argv[1], int(float(sys.argv[2])), int(float(sys.argv[3])))
    except IndexError:
        print("Not all arguments have been provided!")
        print("USAGE: [operation] [start_number] [operation_number]\n")
        raise
    except:
        print("Unknown error! See the details below.\n")
        raise


def main():
    operation, start_number, operation_number = get_args()
    if operation == "add":
        result = add(start_number, operation_number)
    elif operation == "subtract":
        result = subtract(start_number, operation_number)
    elif operation == "multiply":
        result = multiply(start_number, operation_number)
    elif operation == "divide":
        result = divide(start_number, operation_number)
    else:
        raise Exception(f"Unsupported or invalid operation '{operation}'")
    print(result)
    return 0


if __name__ == '__main__':
    sys.exit(main())