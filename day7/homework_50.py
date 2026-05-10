#50、	判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。

str = 'abCdEfg'
is_first_letter_uppercase = str[0].isupper()
is_all_lowercase = str.islower()
is_all_uppercase = str.isupper()
print("首字母大写:", is_first_letter_uppercase)  # 输出结果：首字母大写: False
print("字母全部小写:", is_all_lowercase)  # 输出结果：字母全部小写: False
print("字母全部大写:", is_all_uppercase)