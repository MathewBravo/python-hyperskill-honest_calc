import string


def validate_numbers(x, y) -> bool:
    try:
        float(x)
        float(y)
        return True
    except ValueError:
        return False


def validate_operator(op) -> bool:
    operators = ['+', '-', '*', '/']
    if op in operators:
        return True
    else:
        return False


def ask_for_equation():
    print("Enter an equation")


def process_equation(x, y, op) -> float:
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/' and not (x == 0 or y == 0):
        return x / y


def process_laziness(x: float, y: float, op: string):
    prefix = "You are"
    laziness = [
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
    ]
    message = ""
    if x.is_integer() and y.is_integer():
        if x in range(-10,10) and y in range(-10, 10):
            message = message + laziness[0]
    if (x == 1 or y == 1) and op == '*':
        message = message + laziness[1]
    if (x == 0 or y == 0) and (op == '*' or op == '+' or op == '-'):
        message = message + laziness[2]
    if message != "":
        message = prefix + message
        print(message)


def process_memory_laziness(mem: float) -> bool:
    if mem.is_integer() and mem in range(-10, 10):
        print("Are you sure? It is only one digit! (y / n)")
        nextstep = input()
        if nextstep == 'y':
            print("Don't be silly! It's just one number! Add to the memory? (y / n)")
            nextstep = input()
            if nextstep == 'y':
                print("Last chance! Do you really want to embarrass yourself? (y / n)")
                nextstep = input()
                if nextstep == 'y':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return True
