import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
s=(a+b+c)/2
print('Dien tich=',math.sqrt(s*(s-a)*(s-b)*(s-c)),sep="")