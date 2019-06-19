import operator

print("Enter a math equation! [+, -, *, /, ^]")
print("Hit (q)uit to exit the program.")

op_list = {"+":operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow, '%':operator.mod}


def parse_expression(equation, op_list):
    for operator in op_list:
        op_location = equation.find(operator)
        if op_location >= 1:
            active_op = operator
            first_num = equation[:op_location]
            last_num = equation[op_location+1:]
            return (int(first_num), int(last_num), active_op)


while True:

    equation = str(input(": "))

    if "q" in equation and len(equation) <= 4:
        break

    try:
        first_num, last_num, op = parse_expression(equation, op_list)
        ans = op_list[op](first_num, last_num)
        print("Answer: ", ans)

    except TypeError:
        print("Try using an operator or use two numbers.")

    except ValueError:
        print("Try using one of these operators: [+, -, *, /, ^] or try using numbers. ")

    except ZeroDivisionError:
        print("Don't divide by zero!")    

print("Thanks for using my calculator!")
