#62、	将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，
# 实现左对齐、右对齐和居中效果。

str1 = 'Hello, 我是David'
str2 = 'OK, 好'
str3 = '很高兴认识你'

# 左对齐
print("左对齐:")
print(str1.ljust(20))
print(str2.ljust(20))
print(str3.ljust(20))

# 右对齐
print("\n右对齐:")
print(str1.rjust(20))
print(str2.rjust(20))
print(str3.rjust(20))

# 居中对齐
print("\n居中对齐:")
print(str1.center(20))
print(str2.center(20))
print(str3.center(20))
