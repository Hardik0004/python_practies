import pdb
pdb.set_trace()

list1 = [2, 4, 6, 8, 10, 12]
print("First List ", list1)

list2 = [4, 16, 36, 64, 100, 144]
print("Second List ", list2)

result = zip(list1, list2,)
result_set = set(result)
print(result_set)