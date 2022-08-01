# Using joblib to parallelize tasks

import math
import time
from joblib import Parallel, delayed

def calc_factorials(up_to, is_parallelized = False):
    t1 = time.time()
    if is_parallelized:
        results = Parallel(n_jobs = -1)(delayed(math.factorial)(x) for x in range(up_to))
    else:
        results = [math.factorial(x) for x in range(up_to)]
    t2 = time.time()
    return t2 - t1


print(f"Without joblib: {calc_factorials(10000)}")
print(f"With joblib: {calc_factorials(10000, True)}")