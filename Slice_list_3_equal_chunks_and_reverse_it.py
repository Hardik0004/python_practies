import pdb
pdb.set_trace()

list1 = [12, 34, 54, 75, 89, 90, 77, 28, 33]
print("Original list ", list1)

length = len(list1)
chunk_size = int(length / 3)
start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start, end)

    list_chunk = list1[indexes]
    print("Chunk ", i, list_chunk)

    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size
