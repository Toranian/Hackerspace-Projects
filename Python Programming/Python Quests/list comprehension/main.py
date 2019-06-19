powers_of_2 = [2 ** x for x in range(1, 9)]
print(powers_of_2)

bit_labels = [str(x) + "-bit" for x in range(1, 9)]
print(bit_labels)


bit_info = dict(zip(bit_labels, powers_of_2))
print(bit_info)
