import pdb
pdb.set_trace()


def append(s1, s2):

    print("Original Strings are", s1, s2)
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append("Hardik", "Pansuriya")
