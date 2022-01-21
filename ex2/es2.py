fin = open("ex2/matrix1.dat", "r")
a = []
for line in fin.readlines():
  a.append([int(x) for x in line.split(',')])

print(a[9])

#---------------

import numpy as np
inmat = np.loadtxt("ex2/matrix1.dat", dtype = "i", delimiter = ",")
print(inmat[9])
