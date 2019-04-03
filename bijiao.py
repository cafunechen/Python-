n = int(input())
h = list(map(int,input().split()))
m = int(input())
w = list(map(int,input().split()))
h.sort
w.sort
res = 0
i = 0
j = 0
while (i<m and j<n):
    if w[i]>=h[j]:
        res+=1
        i+=1
        j+=1
    else:
        i+=1
print(res)
