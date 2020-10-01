n = int(input())

ab = str(input())

arr = []

arr = ab.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])


arr = list(set(arr))

print(len(arr))