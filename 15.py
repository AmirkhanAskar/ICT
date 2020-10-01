n = int(input())
a = 0
b = 1
c = 1
arr = []
cnt = 1

res = 0

while(c < n):
    c = a + b
    arr.append(c)
    cnt = cnt + 1
    a = b 
    b = c

for i in range(len(arr)):
    if n == arr[i]:
        res = 1
    else:
        res = 0
if res ==1:
    print(cnt)
elif res == 0:
    print(-1)

 