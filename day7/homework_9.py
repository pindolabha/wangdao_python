#9、	反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
reversed_list = list1[::-1]
index_of_5 = reversed_list.index(5)
print(index_of_5)  # 输出结果：2