#51、	返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。

str = 'this is python'
capitalized_str = str.capitalize()
title_str = str.title()
print("首字母大写:", capitalized_str)  # 输出结果：'This is python'
print("每个单词首字母大写:", title_str)  # 输出结果：'This Is Python'