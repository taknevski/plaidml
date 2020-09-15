import numpy as np
import sys
import time

# Stepping function for conjugate gradient 
def step(A, b, x, r, p, rsold):
    Ap = A @ p
    alpha = rsold / (p.T @ Ap)
    x += alpha*p
    r -= alpha*Ap
    rsnew = r.T @ r
    p = r + p * (rsnew / rsold)
    print(Ap, x, r, p, alpha, rsnew)
    return x, r, p, rsnew

# Computes solution to Ax = b using conjugate gradient method
def conjgrad(A, b, x):
    r = b - A @ x
    p = r.copy()
    rsold = r.T @ r
    for i in range(1):
        x, r, p, rsold = step(A, b, x, r, p, rsold)
    return x

N = int(sys.argv[1])

# Generate a reasonable test system
A = np.empty((N,N))
for i in range(N):
    for j in range(N):
        A[i,j] = N - abs(i-j)
# b = np.random.rand(N,1)
b = np.zeros((N,1))
b[-1] = 1
x0 = np.zeros((N,1))

# Numpy black-box solver
t0 = time.time()
np_x = np.linalg.solve(A, b)
np_tm = time.time() - t0

# Conjugate gradient method
t0 = time.time()
cg_x = conjgrad(A,b,x0)
step_tm = time.time()-t0

print("N: ", N)
print("Numpy Linalg Solution Time: ", np_tm)
print("Conjugate Gradient Solution Time: ", step_tm)
print("Avg. Error: ", np.mean(np.abs((cg_x[abs(np_x)>1e-4]-np_x[abs(np_x)>1e-4])/np_x[abs(np_x)>1e-4])))