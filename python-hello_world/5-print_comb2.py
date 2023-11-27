for a in range(0,100,1):
    if a < 10:
         print("0{}".format(a), end=", ")
    elif a>=10 and a<99:
        print(a, end=", ")
    elif a==99:
        print(a)