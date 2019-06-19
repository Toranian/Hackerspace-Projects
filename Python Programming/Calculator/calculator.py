print("Enter a math equation! [+, -, *, /, ^]")

while True:

    num_list = []
    user_input = str(input(": "))
    ans = None

    if "+" in user_input:
        num_list = user_input.partition("+")
        ans = float(num_list[0]) + float(num_list[2])

    if "-" in user_input:
        num_list = user_input.partition("-")
        ans = float(num_list[0]) - float(num_list[2])

    if "*" in user_input:
        num_list = user_input.partition("*")
        ans = float(num_list[0]) * float(num_list[2])

    if "/" in user_input:
        num_list = user_input.partition("/")
        ans = float(num_list[0]) / float(num_list[2])

    if "^" in user_input:
        num_list = user_input.partition("^")
        ans = float(num_list[0]) ** float(num_list[2])

    if ans == None:
        print("You seemed to have put in an incorrect format.")
    else:
        print(ans)
