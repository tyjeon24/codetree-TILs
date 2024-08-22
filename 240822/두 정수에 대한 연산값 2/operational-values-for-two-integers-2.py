a, b = map(int, input().split())

def modify(a, b):
    if a<b:
        a, b = (a+10, b*2)
    else:
        a, b = (b+10, a*2)
    return a, b
a, b = modify(a, b)
print(a, b)