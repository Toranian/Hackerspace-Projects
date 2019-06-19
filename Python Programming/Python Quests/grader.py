my_final_xp = 493
my_percent = my_final_xp / 10.0
print(my_percent)

if my_percent < 49.5:
    print("F")

if my_percent < 59.5 and my_percent >= 49.5:
    print("C-")

if my_percent >= 59.5 and my_percent <= 66.5:
    print("C")

if my_percent > 66.5 and my_percent < 72.5:
    print("C+")

if my_percent >= 72.5 and my_percent < 85.5:
    print("B")

if my_percent >= 85.5:
    print("A")
