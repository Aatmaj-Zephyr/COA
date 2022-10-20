def convert_to_binary_integer(num):
    arr = []
    while (num != 1):
        arr.append(round(num % 2))
        num = num - num % 2
        num /= 2
    arr.append(1)
    arr = arr[::-1]
    return arr
import math
def IEEE(num):
      signbit=[0]
      if(num<0):
            signbit=[1]
            num=num*-1
      intpart = convert_to_binary_integer(math.floor(num)) #numbers before decimal
      intpart.pop(0) #remove first 1
      floatpart= convert_to_binary_float(num-math.floor(num)) #numbers after decimal
      mantissa=intpart+floatpart
      exponent= len(intpart)
      exponent=exponent+1023 #bais
      exponent=convert_to_binary_integer(exponent)
      print("64 bit representation")
      print("signbit",signbit)
      print("exponent",exponent)
      print("mantissa",mantissa)
      return signbit+exponent+mantissa
def convert_to_binary_float(num):
    arr=[]
    for i in range(0,52):
        num=num*2
        if(num>=1):
            arr.append(1)
            num=num-1
        else:
            arr.append(0)
    return arr
    
print(IEEE(float(input("Decimal Number "))))
