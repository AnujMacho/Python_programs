for i in range(1,21):
    if i == 4 or i == 13:
        print(f"{i} is an Unlucky number")    
    elif i%2 != 0:
        print(f"{i} is an odd number")
    else:
        print(f"{i} is an even number")    