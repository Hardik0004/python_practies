import pdb
pdb.set_trace()

first_number = 0
second_number = 1

print("Fibonaci series")

for i in range(10):
    print(first_number, end="  ")

    next_number = first_number+second_number
    first_number = second_number
    second_number = next_number
