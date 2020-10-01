num = 0
arr = []
res = 0

shower = True

while shower:
    res = res + int(input())
    arr.append(res)
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            shower = False
            
for i in range(len(arr)-1):
    arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i] - arr[len(arr) - 2 - i]

arr.pop()

maximum = max(arr)

cnt = 0

for i in range(len(arr)):
    if maximum == arr[i]:
        cnt = cnt + 1

print(cnt)

