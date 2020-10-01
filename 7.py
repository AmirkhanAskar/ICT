n = float(input())
m = float(input())
x = float(input())
y = float(input())

arr = []

if x >= n/2:
    arr.append(n-x)
else:
    arr.append(x)

if y >= m/2:
    arr.append(m - y)
else:
    arr.append(y)

arr.sort()
print(arr[0])