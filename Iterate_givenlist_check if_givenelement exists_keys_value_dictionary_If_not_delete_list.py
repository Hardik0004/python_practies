import pdb
pdb.set_trace()

roll_number = [47, 43, 55, 75, 76, 12, 69, 97, 23, 4, 64, 10, 29]
sample_dict = {'a': 47, 'b': 69, 'c': 76, 'd': 97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)