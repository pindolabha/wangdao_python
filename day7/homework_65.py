#65、	将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。

str = 'abc'
new_str = ','.join(str)
print("新的字符串:", new_str)  # 输出结果：新的字符串: 'a,b,c'