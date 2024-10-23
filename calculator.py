

#multiplication
def multiplication():
    x = float(input("for x*y, define 'x.' "))
    y = float(input("for x*y, define 'y.' "))
    print(f'{x} times {y} is {x*y}.')
    return

#addition
def addition():
    x = float(input("for x+y, define 'x.' "))
    y = float(input("for x+y, define 'y.' "))
    print(f'{x} plus {y} is {x+y}.')
    return

#subtraction
def subtraction():
    x = float(input("for x-y, define 'x.' "))
    y = float(input("for x-y, define 'y.' "))
    print(f'{x} minus {y} is {x-y}.')
    return

#div: remainder
def remainder():
    x = float(input("for x/y, define 'x.' "))
    y = float(input("for x/y, define 'y.' "))
    print(f' {x} divided by {y} is {x//y} with remainder {x%y}.')
    return

#div: decimal
def decimal():
    x = float(input("for x/y, define 'x.' "))
    y = float(input("for x/y, define 'y.' "))
    print(f'{x} divided by {y} is {x/y}.')
    return

#mode selector
def select():
    mode = input('pick between:\ndivision,\nmultiplication,\naddition,\nsubraction.\nenter the name ')
    if mode == 'multiplication' or mode == 'addition' or mode == 'subtraction' or 'x' or '-' or '+':
        print(f'{mode} selected.')
        if mode == 'multiplication'or '*' or 'x':
            multiplication()
            return
        elif mode == 'subtraction' or '-':
            subtraction()
            return
        elif mode == 'addition' or '+':
            addition()
            return
    elif mode == 'division' or '/':
        mode = input('remainder or decimal? ')
        print(f'{mode} selected.')
        if mode == 'remainder' or 'r':
            remainder()
            return
        elif mode == 'decimal' or 'd':
            decimal()
            return
    else:
        print("try again.")
        select()
        return

#thing that glues the functions together, then does it again
def calc():
    select()
    calc()

#kick starts calculator
calc()
