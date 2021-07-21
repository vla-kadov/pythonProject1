a = 23
b = 12


def f():
    global a
    a = a + 2
    print(a)


f()
print(a)