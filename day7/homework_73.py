#73、	将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。

lst = [3, 'a', 5.2, 4, {}, 9, []]
modified_lst = [1 if isinstance(x, (int, float)) and x > 3 else 0 for x in lst]
print(modified_lst)  # 输出结果：[0, 0, 1, 1, 0, 1, 0]，表示列表中大于3的整数或浮点数被置为1，其余被置为0的结果