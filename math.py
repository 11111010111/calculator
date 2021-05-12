operators = ["+", "-", "*", ".", "/", "**", "sqrt", "%", "<", "=", ">", "=/=", "//", "crt"]


def the_actual_math(first, operation, second):
    if operation == operators[0]:
        result = float(first) + float(second)
    elif operation == operators[1]:
        result = float(first) - float(second)
    elif operation == (operators[2]):
        result = float(first) * float(second)
    elif operation == operators[4]:
        result = float(first) / float(second)
    elif operation == "**":
        result = float(first) ** float(second)
    elif operation == "crt":
        result = "currently broken sorry, i will fix this sometime"
    elif operation == "sqrt":
        result = "currently broken sorry, i will fix this sometime"
    elif operation == "%":
        result = float(first) % float(second)
    elif operation == "//":
        result = float(first) // float(second)
    elif operation == "<":
        if first < second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed less than " + second)
        else:
            result = (first + " is not less than " + second)
    elif operation == "=":
        if first == second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed equal to " + second)
        else:
            result = (first + " is not equal to " + second)
    elif operation == ">":
        if first > second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed more than " + second)
        else:
            result = (first + " is not more than " + second)
    elif operation == "=/=":
        if first != second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed not equal to " + second)
        else:
            result = (first + " is indeed equal to " + second)
    else:
        result = 0
    return result
