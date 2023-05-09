#for x in range(8):
#    for y in range(x):
#        print(y,end=" ")
#    print()

def num(n):
    for x in range(1,n+1):
        for y in range(1,x + 1):
            print(y, end=" ")
        print()

num(8)