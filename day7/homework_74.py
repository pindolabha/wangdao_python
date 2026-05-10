#74、	将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。

two_dimensional_list = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
one_dimensional_list = [element for sublist in two_dimensional_list for element in sublist]
print(one_dimensional_list)  # 输出结果：[1, 'a', 'b', 2.3, 4.5, 6.7]，表示二维列表被转为一维列表的结果