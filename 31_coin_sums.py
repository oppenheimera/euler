"""1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)"""
import time

start = time.time()

def c_d(targ):
    """this doesn't work for targ=200"""
    if targ == 0:
        return 1
    if targ < 0:
        return 0
    else:
        return c_d(targ - 200) + c_d(targ - 100) + c_d(targ - 50) + c_d(targ - 20) + c_d(targ - 10) + c_d(targ - 10) + c_d(targ - 5) + c_d(targ - 2) + c_d(targ - 1)

# ans = cd(200)
elapsed = time.time() - start

print("Found {} in  {} seconds.".format(ans, elapsed))
