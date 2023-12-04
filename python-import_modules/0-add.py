from add_0 import add
a= 1
b= 2


if __name__ == "__main__":
 
 if a==1 and b==2:
    print("1 + 2 = {}".format(add(a,b)))
 else:
    print("{} + {} = {}".format((a,b),add(a,b)))

