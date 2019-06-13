def find_factors(num):
    list1 = []
    for a in range(1, num+1):
        if num%a == 0:
            list1.append(a)
    return list1

find_factors(10)