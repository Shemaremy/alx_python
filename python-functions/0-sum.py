#
def add(a, b):
    s=a+b
    print(s)
    return s
add = __import__('0-sum').add

add(1,2)
