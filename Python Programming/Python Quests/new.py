
fives = [x for x in range(10, 30, 5)]
print(fives)

assignment_marks = {"Homework 1": 5, "Homework 2": 4, "Quiz 1": 4, "Test 1": 10}

homework_marks = 0
for key in assignment_marks.keys():
    if "homework" in key.lower():
        homework_marks += assignment_marks[key]

print("total score: " + str(homework_marks))
