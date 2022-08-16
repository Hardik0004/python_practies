import pdb
pdb.set_trace()

list1 = [12, 32, 43, 55, 99, 19, 50, 38, 50, 20, 50]
print("Original list ", list1)

count_dict = dict()
for item in list1:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)
