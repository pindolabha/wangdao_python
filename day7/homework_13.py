#13、	删除列表中索引号为奇数（或偶数）的元素。
list1 = [True, 1, 0, 'x', None, 'x', False, 2, True]
# 删除索引号为奇数的元素
list2 = [elem for idx, elem in enumerate(list1) if idx % 2 == 1]
print(list2)  # 输出结果：[1, 'x', 'x', 2]
# 删除索引号为偶数的元素
list3 = [elem for idx, elem in enumerate(list1) if idx % 2 == 0]
print(list3)  # 输出结果：[True, 0, None, False, True]