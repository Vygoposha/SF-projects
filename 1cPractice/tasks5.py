L = [i for i in range(10)]
M = [i for i in range(10,0,-1)]
N = [ ]

for i in range(10):
    N.append(L[i] * M[i])
#print(N)
for a in zip(L,M):
    print(a)
for a, b in zip(L,M):
    print(a*b)
N = [a*b for a,b in zip(L,M)]
print(N)