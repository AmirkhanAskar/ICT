n = int(input())
sq = str(input())

arr = []
arr = sq.split()
spare = arr[len(arr) - 1]
another = []
another.append(spare)
arr.pop()

for i in range(len(arr)):
    another.append(arr[i])

    
print(another)

