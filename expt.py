
def convert_to_binary(num):
    
        
    return 0
def complement(num):
    for i in range(0,x):
        if(x[i]==0)
    return 0
def shift_right(c):
    c.pop()
    c.insert(0,c[0])
    return c
def add(x,y):
    z=[]
    for i in range(0,len(x)):
        z.append(x[i]+y[i])
    return z
a=[1,1,0,1,0] #-6

a_=[0,0,1,1,0]#+6

b=[1,1,1,0,0] #-4
b_=[0,0,1,0,0]

c=[0,0,0,0,0]+b+[0]
print(c)
"""print(c)
c=shift_right(c)
print(add(a,b))"""
for i in range(0,5):
    if(c[-1]>c[-2]):
        c=add(c[0:5],a)+c[5:]
    if(c[-1]<c[-2]):
       c=add(c[0:5],a_)+c[5:]
    c=shift_right(c)
    print(c)
c=c[5:-1]
print(c)
    
    
