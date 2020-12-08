N,M,Q = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(M)]
pq = [list(map(int,input().split())) for _ in range(Q)]
cut = [[0 for i in range(N)] for j in range(N)]
sum = 0
for k in range(M):
    cut[LR[k][0]-1][LR[k][1]-1] += 1
for q in range(Q):
    for l in range(pq[q][0],pq[q][1]+1):
        for r in range(pq[q][1],pq[q][0]-1,-1):
            sum += cut[l-1][r-1]
            if l >= r:
                break
    print(sum)
    sum = 0
