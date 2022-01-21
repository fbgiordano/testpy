import numpy as np
import scipy
#import matplotlib as mpl
#import matplotlib.pyplot as plt

a = np.arange(10)
b = np.zeros_like(a)
b[:] = a[:]
print(a)
print(b)