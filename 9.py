a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

arr1 = []
arr2 = []

arr1.append(a1)
arr1.append(b1)
arr1.append(c1)

arr2.append(a2)
arr2.append(b2)
arr2.append(c2)

arr1.sort()
arr2.sort()

if (arr1[0] / arr2[0]) >= 2 and arr1[1]==arr2[1] and arr1[2]==arr2[2]:
    print("first box is bigger than the second one")
elif arr1[0] == arr2[0] and (arr1[1]/arr2[1]) >= 2 and arr1[2]==arr2[2]:
    print("first box is bigger than the second one")
elif arr1[0] == arr2[0] and arr1[1]==arr2[1] and (arr1[2]/arr2[2]) >= 2:
    print("first box is bigger than the second one")
elif (arr2[0]/arr1[0]) >= 2 and arr2[1]==arr1[1] and arr2[2]==arr1[2]:
    print("senod box is bigger then the fist one")
elif arr2[0]==arr1[0] and (arr2[1]/arr1[1]) >= 2 and arr2[2]==arr1[2]:
    print("senod box is bigger then the fist one")
elif arr2[0]==arr1[0] and arr2[1]==arr1[1] and (arr2[2]/arr1[2]) >= 2:
    print("senod box is bigger then the fist one")
else:
    print("Boxes are equal")