def truncate(str1, num):
    list1 = []
    if num<3:
        return "Truncation must be at least 3 characters."
    elif num>len(str1):
        return str1
    else:
        for a in str1:
            list1.append(a)
        list1 = list1[:num-3]
    return "".join(list1)+"..."

truncate("Problem solving is the best!", 10)