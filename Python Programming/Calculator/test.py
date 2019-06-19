monty_python_birth_years = { "John": 1939, "Eric": 1943, "Graham": 1941, "Terry": 1940,}

who = input("Who's birth year do you want to know? ")

try:
    year = monty_python_birth_years[who]
    print("{} was born in {}".format(who, year))

except KeyError:
    print("That year is not recognized.")
