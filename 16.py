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

cnt = 0

for i in range(len(arr)-1):
    if arr[i+1] > arr[i] and arr[i+1] > arr[i+2]:
        cnt = cnt+ 1

print(cnt)