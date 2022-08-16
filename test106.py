set1 = {10, 20, 30, 40, 50}
set2 = {50, 60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("The Two Set have no item in common")

else:
    print("The Two set have item in common")
    print(set1.intersection(set2))