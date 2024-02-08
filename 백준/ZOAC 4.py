import math

H, W, N, M = map(int, input().split())

# 앉을 수 있는 자리의 개수 : 길이/ 간격+1
row = math.ceil(H/(N+1))
col = math.ceil(W/(M+1))

print(row*col)