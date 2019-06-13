def range_in_list(list1, start=0, end=None):
    if end == None or end > len(list1):
        end = len(list1)
    lst = list1[start:end+1]
    sum = 0
    for a in lst:
        sum = sum + a
    print(sum)

range_in_list([1,2,3,4],0,2)