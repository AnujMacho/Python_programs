def sum_pairs(list1, num):
    list2 = []
    for a in list1:
        for b in reversed(list1):
            if a+b == num:
                list2.append(a)
                list2.append(b)
    list2 = list2[:2]
    return list2

print(sum_pairs([3, 6, 4, 1], 8))