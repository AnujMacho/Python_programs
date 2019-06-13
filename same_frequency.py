def same_frequency(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    lst = []
    for a in num1:
        if num1.count(a) == num2.count(a):
            lst.append(a)

    if(len(lst) == len(num1)):
        return True
    else:
        return False

print(same_frequency(551122,221515))