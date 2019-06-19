print("Enter a math equation! [+, -, *, /, ^]")
print("Hit (q)uit to exit the program.")

op_list = ["+", '-', '*', '/', '^']


while True:

    num_list = []
    user_input = str(input(": "))
    ans = None

    for op in op_list:
        if op in user_input:
            operator = op

    if "q" in user_input:
        break

    if "+" == operator:
        num_list = user_input.partition("+")
        ans = float(num_list[0]) + float(num_list[2])

    if "-" == operator:
        num_list = user_input.partition("-")
        ans = float(num_list[0]) - float(num_list[2])

    if "*" == operator:
        num_list = user_input.partition("*")
        ans = float(num_list[0]) * float(num_list[2])

    if "/" == operator:
        num_list = user_input.partition("/")
        ans = float(num_list[0]) / float(num_list[2])

    if "^" == operator:
        num_list = user_input.partition("^")
        ans = float(num_list[0]) ** float(num_list[2])

    if ans == None:
        print("You seemed to have put in an incorrect format.")
    else:
        # print("{} {} {} = {}".format(user_input[0], user_input[1], user_input[2], ans))
        print("Answer: ", ans)

print("Thanks for using my calculator!")
