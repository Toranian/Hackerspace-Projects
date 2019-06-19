print("Enter a math equation! [+, -, *, /, ^]")
print("Hit (q)uit to exit the program.")

op_list = ["+", '-', '*', '/', '^']


def parse_expression(equation, op_list):
    for operator in op_list:
        op_location = equation.find(operator)
        if op_location >= 1:
            active_op = operator
            first_num = equation[:op_location]
            last_num = equation[op_location+1:]
            return (first_num, last_num, active_op)

def calculate(first_num, last_num, operator):
    
    if "+" == operator:
        num_list = equation.partition("+")
        ans = float(first_num) + float(last_num)

    if "-" == operator:
        num_list = equation.partition("-")
        ans = float(first_num) - float(last_num)

    if "*" == operator:
        num_list = equation.partition("*")
        ans = float(first_num) * float(last_num)

    if "/" == operator:
        num_list = equation.partition("/")
        ans = float(first_num) / float(last_num)

    if "^" == operator:
        num_list = equation.partition("^")
        ans = float(first_num) ** float(last_num)

    else:
        return ans

while True:

    equation = str(input(": "))

    if "q" in equation:
        break

    try:
        first_num, last_num, operator = parse_expression(equation, op_list)
        ans = calculate(first_num, last_num, operator)
        print("Answer: ", ans)

    except:
        print("You seemed to have put in an incorrect format.")


print("Thanks for using my calculator!")
