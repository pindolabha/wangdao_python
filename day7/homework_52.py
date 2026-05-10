#52、	判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。

str = 'this is python'
starts_with_this = str.startswith('this')
ends_with_python = str.endswith('python')
print("以 'this' 开头:", starts_with_this)  # 输出结果：以 'this' 开头: True
print("以 'python' 结尾:", ends_with_python)  # 输出结果：以 'python' 结尾: True