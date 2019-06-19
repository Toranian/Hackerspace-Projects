minor_words = [ "lots", "maybe", "uncertain", "perhaps", ]
major_words = ["don't", "you", "I", "we", "our", "?", "mine", "myself", "my", ]
minor_errors = []
major_errors = []

file = open("essay.txt", "r")
errors = 0


for line in file:
    for word in line.split():
        if word in minor_words:
            minor_errors.append(word)
            
        if word in major_words:
            major_errors.append(word)


if len(major_errors) > 0:
    print("Major Errors:\n")
    for e in major_errors:
        print(e)  
    print("\nThis is an error because essays should be written in THIRD person, and not in second or first!")


if len(minor_errors) > 0:
    print("\nMinor Errors:\n")
    for e in minor_errors:
        print(e)
    print("\nThis is an error because these words tend to show opinion and not facts.")

if len(major_errors) == len(minor_errors) and len(major_errors) == 0:
    print("No errors! Your essay is perfect! :)")