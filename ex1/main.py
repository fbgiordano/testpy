import math
import time

a = list(range(10000000))
b = list(range(5000000))
t1 = time.time()
z = a+b
t2 = time.time()
y = a.extend(b)
t3 = time.time()

print(t2-t1)
print(t3-t2)