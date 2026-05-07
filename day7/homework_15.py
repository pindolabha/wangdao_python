#15、	对列表 [3,0,8,5,7] 分别做升序和降序排列。
list1 = [3, 0, 8, 5, 7]
# 升序排列
sorted_list_asc = sorted(list1)
print("升序排列:", sorted_list_asc)  # 输出结果：升序排列: [0, 3, 5, 7, 8]
# 降序排列
sorted_list_desc = sorted(list1, reverse=True)
print("降序排列:", sorted_list_desc)  # 输出结果：降序排列: [8, 7, 5, 3, 0]