import pdb
pdb.set_trace()

print(" Enter The number ")

a = int(input())
input_number = a

for i in range(1, input_number+1):

    print("Current Number is :", i, " and the cube is", (i * i * i))
