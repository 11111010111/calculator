operators = ["+", "-", "*", ".", "/", "**", "sqrt", "%", "<", "=", ">", "=/=", "//", "crt"]


def sqrt(a):
    b = float(a) ** 0.5
    return b


def crt(a):
    b = float(a) ** (1/3)
    return b


def the_actual_math(first, operation, second):
    first = float(first)
    second = float(second)
    if operation == operators[0]:
        result = first + second
    elif operation == operators[1]:
        result = first - second
    elif operation == (operators[2]):
        result = first * second
    elif operation == operators[4]:
        result = first / second
    elif operation == "**":
        result = first ** second
    elif operation == "crt":
        result = crt(first)
    elif operation == "sqrt":
        result = sqrt(first)
    elif operation == "%":
        result = first % second
    elif operation == "//":
        result = first // second
    elif operation == "<":
        if first < second:
            result = True
        else:
            result = False
        if result:
            result = (str(first) + " is indeed less than " + str(second))
        else:
            result = (str(first) + " is not less than " + str(second))
    elif operation == "=":
        if first == second:
            result = True
        else:
            result = False
        if result:
            result = (str(first) + " is indeed equal to " + str(second))
        else:
            result = (str(first) + " is not equal to " + str(second))
    elif operation == ">":
        if first > second:
            result = True
        else:
            result = False
        if result:
            result = (str(first) + " is indeed more than " + str(second))
        else:
            result = (str(first) + " is not more than " + str(second))
    elif operation == "=/=":
        if first != second:
            result = True
        else:
            result = False
        if result:
            result = (str(first) + " is indeed not equal to " + str(second))
        else:
            result = (str(first) + " is indeed equal to " + str(second))
    else:
        result = 0
    return result
