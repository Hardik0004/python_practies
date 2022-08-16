import pdb
pdb.set_trace()

Given_number = [12, 75, 150, 180, 145, 525, 50]


for item in Given_number:

    if item > 500:
        break

    elif item > 150:
        continue

    elif item % 5 == 0:

        print(item)
