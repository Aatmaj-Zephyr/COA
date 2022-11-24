Memorysize = int(input('please enter Memory size in k words  ')) * 1024

cachesize = int(input('please enter cache size in k words ')) * 1024

import math

tag = math.log2(Memorysize / cachesize)
block = math.log2(Memorysize)
word = Memorysize / cachesize / block

print("tag ", tag)
print("block ", block)
print("word ", word)
