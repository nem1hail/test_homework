

def multiplication():
    i = 1
    j = 1

    while i < 10:
        while j < 10:
            print(i * j, end='\t')
            j += 1
        print('\n')
        j = 1
        i += 1
def iterations():
    fathers = ['John', 'Michael', 'David']
    iter_rule = iter(fathers)
    try:
        while True:
            next_value = next(iter_rule)
            print(next_value)
    except StopIteration:
        print("Iteration has ended.")
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /, stop): ")

            if operation == 'stop':
                break
            elif operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero.")
                    return
            else:
                print("Invalid operation.")
                return

            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def generator():
    import random
    def conveyor():
        while True:
            yield random.randint(95, 105)
    factory = conveyor()
    defective_count = 0
    for detail_size in factory:
        if detail_size < 98 or detail_size > 102:
            defective_count += 1
        print(f"Detail size: {detail_size}")
        if defective_count >= 3:
            print("Too many defective details. Stopping production.")
            break

generator()
#do homework
