n = int(input())
total = 10**n-1
stair = []
im = []
check = 0
aws = 0

for i in range(10**(n-1), total+1):
    im = list(str(i))
    for jari in range(n-1):
        if abs(int(im[jari])-int(im[jari+1]))==1:
            check += 1
        else:
            check = 0
    if check == n-1:
        stair.append(i)


print(len(stair)%1000000000)