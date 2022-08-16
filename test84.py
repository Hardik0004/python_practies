import pdb
pdb.set_trace()

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400, 500, 600, 700]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

print("New List : ")

for a, b in zip(list1, list2[::1]):
    print(a, b)