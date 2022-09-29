# restoring division for unsigned integer
# works for range 1-15
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
    if (len(arr) < 4):
        while (len(arr) != 4):
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


def shift_left(c):
    c.pop(c[0])
    c.insert(-1, c[-1])
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


a = convert_to_binary(int(input()))  #-6
print(a)
b = convert_to_binary(int(input()))

c = [0] + [0, 0, 0, 0] + b
print(c)

for i in range(0, 4):
    if(c[0]==0):
       c=shift_left(c)
       c[0:5]=add(c[0:5], [complement(a)[0]] +
               complement(a))#add one extrabit (repeat sign bit)
    elif(c[0]==1):
       c=shift_left(c)
       c[0:5]=add(c[0:5], [a[0]] +
               a)#add one extrabit (repeat sign bit)
    if(c[0]==0):
        c[-1]=1
    elif(c[0]==1):
        c[-1]=0
    print(c)
if(c[0]==1):
         c[0:5]=add(c[0:5], [a[0]] +
               a)#add one extrabit (repeat sign bit)
print(c[0:5])
print(c[5:])
