def titleize(str1):
    list1 = []
    str2 = str1.split(" ")
    for a in str2:
        b = a[0].upper()+a[1:]
        list1.append(b)
    str2 = " ".join(list1)
    return str2

print(titleize('this is awesome'))