try:
    input_file = open("input_file.txt", 'r')
    output_file = open("output_file.txt", 'w')

except:
    print("File doesn't exist! Go away!")
    quit()

for line in input_file:
    line = line.lower()
    if "king" in line and "arthur:" in line:
        output_file.write(line)
        print(line)

input_file.close()
output_file.close()
