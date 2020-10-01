a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a2 - a1) ==  2  and b1 == b2:
    print ("YES")
elif (a2 - a1) ==  -2 and b1 == b2:
    print ("YES")
elif (b2 - b1) == 1 and a2 == a1:
    print("YES")
elif (b2 - b1) == -1 and a2 == a1:
    print("YES")
else:
    print("NO")