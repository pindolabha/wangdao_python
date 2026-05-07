#19、	分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。
list2d = [[6, 5], [3, 7], [2, 8]]
# 根据每一行的首元素大小排序
sorted_by_first = sorted(list2d, key=lambda x: x[0])
print("根据首元素排序:", sorted_by_first)  # 输出结果：根据首元素排序: [[2, 8], [3, 7], [6, 5]]
# 根据每一行的尾元素大小排序
sorted_by_last = sorted(list2d, key=lambda x: x[1])
print("根据尾元素排序:", sorted_by_last)  # 输出结果：根据尾元素排序: [[6, 5], [3, 7], [2, 8]]