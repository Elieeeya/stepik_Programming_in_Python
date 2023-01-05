# https://stepik.org/lesson/5047/step/1?unit=1086

import math
a = int (input())
b = int (input())
c = int (input())
p = (a+b+c)/2
S = math.sqrt(p * (p-a) * (p-b) * (p-c))
print(S)