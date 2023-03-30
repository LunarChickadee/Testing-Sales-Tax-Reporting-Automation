
import numpy as np
import pandas as pd


# Python program to demonstrate
# indexing in numpy

 
# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
 
# Slicing array
temp = arr[:2, ::2]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)


temp=arr[0:1, ::2]
print("\n",temp)