n = int(input())
cnt = 0
arr = []
res = ''
while(n >= 1):
    n = n/2
    cnt +=1

for i in range(cnt):
    arr.append(2**i)

print(arr)
