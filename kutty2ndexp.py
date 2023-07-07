str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
i1 = 0
i2 = 0
while i1 < len(str1) and i2 < len(str2):
       if str1[i1] == str2[i2]:
        i1 += 1
        i2 += 1
       else:
        i1 += 1
if i2 == len(str2):
    print("YES")
else:
    print("NO")
