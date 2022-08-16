import pdb
pdb.set_trace()

a = 5
b = 5

for i in range(0, a+1):

    for j in range(b-i, 0, -1):

        print(j, end=" ")

    print("")
