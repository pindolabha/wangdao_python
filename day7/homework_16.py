#16、	将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0。
list1 = [3, 0, 8, 5, 7]
list1 = [1 if x > 5 else 0 for x in list1]
print(list1)  # 输出结果：[0, 0, 1, 0, 1]