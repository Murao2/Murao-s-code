import math

S = int(input())
K = int(input())
SS = []
ste = S
N = math.floor(math.log10(S))
for _ in range(N+1):
    SS.insert(0,ste % 10)
    ste = math.floor(ste/10)
print(SS)
print(N)
for j in range(K):
    che = SS[j]
    if SS[j] != 1:
        che = SS[j]
        break
print(che)
