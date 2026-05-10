#48、	去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。

arr = [1, 2, 5, 2, 3, 4, 5, 'x', 4, 'x']
unique_elements = list(set(arr))
print(unique_elements)  # 输出结果：['x', 1, 2, 3, 4, 5]，表示数组中去除重复元素后的结果