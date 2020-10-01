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
            print(arr[i])
    



        