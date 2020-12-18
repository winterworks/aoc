from sympy import *
import re
import functools

data_file = open('./data/data18')
rows = data_file.read().split('\n')
data_file.close()

def calculate(calculation, order):
    parts = calculation.split(' ')

    # Compute al operators for the given order
    for operator in order:
        for index in range(len(parts)-1,-1,-1):
            if parts[index] == operator:
                parts[index-1] = str(sympify(''.join(parts[index-1:index+2])))
                del parts[index:index+2]

    # Compute the remaing operators normally
    while len(parts) > 2:
        calc_part = parts[0:3]
        del parts[1:3]
        parts[0] = str(sympify(''.join(calc_part)))
    return parts[0]

def parse_calculation(calculation, order = []):
    # find the most inner brakcets and replace these whith their solutions
    while calculation.find('(') > -1:
        inner_brackets = list(re.findall('\((( |\*|\+|\d*)*)\)', calculation))
        inner_brackets_ranges = list(re.finditer('\((( |\*|\+|\d*)*)\)', calculation))
        for index, inner_brackets_range in enumerate(reversed(inner_brackets_ranges)):
            inner_calculation = inner_brackets[index][0]
            split = calculation.split('('+inner_calculation+')', 1)
            calculation = calculate(inner_calculation, order).join(split)

    return int(calculate(calculation, order))

print(sum(list(map(functools.partial(parse_calculation), rows))))
print(sum(list(map(functools.partial(parse_calculation, order=['+', '*']), rows))))