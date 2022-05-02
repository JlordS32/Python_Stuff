y = 4


def test():
    globy = y
    print(globy)

    globy+=1
    print(globy)
test()

x = 0

def test1():
    global x
    x=4
    print(x)

test1()
print(x)