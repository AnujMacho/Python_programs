def repeat(str1, num):
    list1 = []
    for a in range(num):
        list1.append(str1)
    return ("").join(list1)

print(repeat('*', 3))