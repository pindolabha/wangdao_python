n = int(input("请输入一个整数:"))
sum = 0
bitNum = 64

while bitNum > 0 and n != 0:
    if(n & 1 == 1):
        sum += 1
    n = n >> 1
    bitNum -= 1

print(sum)