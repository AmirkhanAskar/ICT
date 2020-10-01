n = int(input())
arr = []
for i in range(2, n+1):
    if n%i == 0:
        arr.append(i)

arr.sort()
print(arr[0])