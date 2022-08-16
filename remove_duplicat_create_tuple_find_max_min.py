import pdb
pdb.set_trace()

sample_list = [22, 34, 54, 66, 54, 25, 99, 32, 1, 33, 22, 45, 64, 54, 25]
print("Original list", sample_list)

sample_list = list(set(sample_list))
print("Unique list", sample_list)

t = tuple(sample_list)
print("Tuple ", t)

print("Minimum Number is: ", min(t))
print("Maximum Number is: ", max(t))
