#20、	从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
list1 = [1, 4, 7, 2, 5, 8]
list2 = ['x', 'y', 'z']
index = 3
for i, elem in enumerate(list2):
    list1.insert(index + i, elem)
print(list1)  # 输出结果：[1, 4, 7, 'x', 'y', 'z', 2, 5, 8]