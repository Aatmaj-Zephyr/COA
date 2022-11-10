SIZE=4
memory=[]
hit=0
def add(a):
    global  hit


    if(len(memory)==SIZE):

        if(a in memory):
            hit=hit+1
            memory.remove(a)
        else:
            memory.pop(-1)
    memory.insert(0,a)
    print(memory)
add(1)        
add(2)
add(3)
add(5)
add(1)
add(4)
add(4)
print(hit)
