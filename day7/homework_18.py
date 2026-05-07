#18、	将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [x for x in list1 if x % 2 != 0]
even_numbers = [x for x in list1 if x % 2 == 0]
print("奇数组:", odd_numbers)  # 输出结果：奇数组: [1, 3, 5, 7, 9]
print("偶数组:", even_numbers)  # 输出结果：偶数组: [0, 2, 4, 6,