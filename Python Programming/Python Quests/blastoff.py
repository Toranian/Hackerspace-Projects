for i in range(5, 0, -1):
    print(i)
print("Blastoff!")


some_text = ["xyz","no z's here!", "zzz", "the letter that shall not be named is not here"]

count = 0
for word in some_text:
    count += word.count('z')


print("Number of Z's: {}".format(count))
