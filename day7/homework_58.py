#58、	判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母？ 

str = 'adS12K56'
is_alphanumeric = str.isalnum()
is_all_digits = str.isdigit()
is_all_alpha = str.isalpha()
print("字符串 'adS12K56' 是否完全为字母数字:", is_alphanumeric)  # 输出结果：字符串 'adS12K56' 是否完全为字母数字: True
print("字符串 'adS12K56' 是否全为数字:", is_all_digits)  # 输出结果：字符串 'adS12K56' 是否全为数字: False
print("字符串 'adS12K56' 是否全为字母:", is_all_alpha)  # 输出结果：字符串 'adS12K56' 是否全为字