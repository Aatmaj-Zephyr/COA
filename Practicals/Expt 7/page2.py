SIZE=4
memory=[]
hit=0
def add(a):
    global  hit


    if(len(memory)!=SIZE):
         memory.insert(0,a)
         print(memory)
         return
    if(a in memory):
        hit+=1
        print(memory)
        return
    else:
         memory.insert(0,a)
         memory.pop(-1)
         print(memory)
    
add(1)        
add(2)
add(3)
add(5)
add(1)
add(4)
add(4)
print(hit)
