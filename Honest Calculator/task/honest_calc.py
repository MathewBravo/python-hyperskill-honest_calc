from memory import Memory
from menu_handler import (ask_for_equation, validate_numbers, validate_operator, process_equation, process_laziness, process_memory_laziness)

if __name__ == '__main__':
    continue_calc = True
    M = Memory(0)
    while continue_calc:
        ask_for_equation()
        x, op, y = input().split()
        if x == 'M':
            x = M.result
        if y == 'M':
            y = M.result
        if validate_numbers(x, y):
            x = float(x)
            y = float(y)
        else:
            print("Do you even know what numbers are? Stay focused!")
        if not validate_operator(op):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        process_laziness(x, y, op)
        if op == '/' and (x == 0 or y == 0):
            print("Yeah... division by zero. Smart move...")
            continue
        result = process_equation(x, y, op)
        print(result)
        print("Do you want to store the result? (y / n):")
        choice = input()
        if choice == 'y':
            if process_memory_laziness(result):
                M.result = result
        print("Do you want to continue calculations? (y / n):")
        choice = input()
        if choice == 'n':
            continue_calc = False
