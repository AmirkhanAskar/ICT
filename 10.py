import math
n = int(input())
arr = []
main = math.floor(math.sqrt(n))
for i in range(1, main+1):
    arr.append(int(math.pow(i, 2)))

print(arr)