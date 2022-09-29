def convert_to_binary(num):
    if (num < 0):
        return complement(convert_to_binary(-num))
    arr = []
    while (num != 1):
        arr.append(round(num % 2))
        num = num - num % 2
        num /= 2
    arr.append(1)
    arr = arr[::-1]
    if (len(arr) < 5):
        while (len(arr) != 5):
            arr.insert(0, 0)
    return arr


def complement(x):
    num = []
    one = []  #array  eg 0001
    for i in range(0, len(x)):
        one.append(0)
        if (x[i] == 0):
            num.append(1)
        if (x[i] == 1):
            num.append(0)
    one.pop()
    one.append(1)
    num = add(num, one)
    return num


def shift_right(c):
    c.pop()
    c.insert(0, c[0])
    return c


def add(x, y):
    carry = 0
    z = []
    x = x[::-1]
    y = y[::-1]
    for i in range(0, len(x)):
        temp = x[i] + y[i] + carry
        carry = 0
        if (temp == 2):
            carry = 1
            temp = 0
        if (temp == 3):
            carry = 1
            temp = 1
        z.append(temp)
    z = z[::-1]
    return z


a_ = convert_to_binary(int(input()))  #-6
print(a_)
a = complement(a_)  #-6

b = convert_to_binary(-int(input()))  #- ve sign because ioot works ??

c = [0, 0, 0, 0, 0] + b + [0]
print(c)
"""print(c)
c=shift_right(c)
print(add(a,b))"""
for i in range(0, 5):
    if (c[-1] > c[-2]):
        c = add(c[0:5], a) + c[5:]
    if (c[-1] < c[-2]):
        c = add(c[0:5], a_) + c[5:]
    c = shift_right(c)
    print(c)
c = c[5:-1]
print(c)
