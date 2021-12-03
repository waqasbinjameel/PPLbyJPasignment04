list = [1, 4, 5, 3, 2, 3, 4, 5, 4]
duplicate_list = []
for i in list:
    if i not in duplicate_list:
        duplicate_list.append(i)
    else:
        print(i, end=' ')