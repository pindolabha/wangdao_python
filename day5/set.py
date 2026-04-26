list = [1, 1, 2, 2, 3]
set = set()
for num in list:
    if num not in set:
        set.add(num)
    else:
        set.remove(num)
print(set)