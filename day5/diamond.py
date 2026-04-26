n = 5

# 实心菱形
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join("*" * i))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + " ".join("*" * i))

print()

# 空心菱形（中间为空白，仅轮廓为 *）
m = n - 1
for i in range(2 * m + 1):
    pad = abs(i - m)
    if i == 0 or i == 2 * m:
        print(" " * pad + "*")
    else:
        inner = 2 * min(i, 2 * m - i) - 1
        print(" " * pad + "*" + " " * inner + "*")
