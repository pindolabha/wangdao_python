#61、	将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、
# 右对齐和居中对齐效果。

# 左对齐
str1 = 'ok'
str2 = 'hello'
str3 = 'thank you'
print("左对齐:")
print(str1.ljust(20))  # 输出结果：左对齐: 'ok                 '
print(str2.ljust(20))  # 输出结果：左对齐: 'hello              '
print(str3.ljust(20))  # 输出结果：左对齐: 'thank you          '

# 右对齐
print("\n右对齐:")
print(str1.rjust(20))  # 输出结果：右对齐: '                 ok'
print(str2.rjust(20))  # 输出结果：右对齐: '              hello'
print(str3.rjust(20))  # 输出结果：右对齐: '          thank you'

# 居中对齐
print("\n居中对齐:")
print(str1.center(20))  # 输出结果：居中对齐: '       ok         '
print(str2.center(20))  # 输出结果：居中对齐: '      hello       '
print(str3.center(20))  # 输出结果：居中对齐: '    thank you     '  