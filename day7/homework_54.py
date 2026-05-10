#54、	返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。

str = 'this is python'
first_occurrence = str.find('is')
last_occurrence = str.rfind('is')
print("字符串 'this is python' 中 'is' 首次出现的位置:", first_occurrence)  # 输出结果：字符串 'this is python' 中 'is' 首次出现的位置: 2
print("字符串 'this is python' 中 'is' 最后一次出现的位置:", last_occurrence)  # 输出结果：字符串 'this is python' 中 '