#branch1
#method1
import time
start = time.time()
import numpy as np

X = np.arange(12).reshape(2, 2, 3)
print(X)
out = np.array(list(map(lambda x: np.array(np.meshgrid(*x)).T.reshape(-1,2), X)))
print(out)


end = time.time()
print(end - start)

#method2
import time
start = time.time()

def meshgrid_2D_blocks(X):
    m,n,r = X.shape
    out_shp = [m]+[r]*n+[n]
    out = np.empty(out_shp,dtype=X.dtype)

    # Assign each block iteratively
    shp = [-1]+[1]*n
    for i in range(n):
        shp[i+1] = r
        out[...,i] = X[:,i].reshape(shp)
        shp[i+1] = 1
    return out.reshape(m,-1,n)

X = np.arange(12).reshape(2, 2, 3)
match = meshgrid_2D_blocks(X)
print(match)

att = np.arange(18).reshape(9,2)
print(att)
print(np.power(match,att))


end = time.time()
print(end - start)

#method3
import time
start = time.time()

X = np.arange(12).reshape(2, 2, 3)
print(X)
out = np.array([np.array(np.meshgrid(*X[m]), dtype=object).T.reshape(-1,2) for m in range(2)])   
print(out)

end = time.time()
print(end - start)
