n = int(input())
numbers = str(input())

arr = []
arr =numbers.split()
cnt = 0 

for i in range(len(arr)):
    arr[i] = int(arr[i])

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            cnt = cnt + 1

print(cnt)