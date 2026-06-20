import numpy as np 

arr1 = np.array([12, 13, 11, 10, 13])
arr1

arr1.shape
arr1.ndim
arr1.size
arr1.itemsize
arr1.dtype
arr2 = arr1.astype(str)
arr2.itemsize

import sys
sys.getsizeof("12")*len(arr1)
