#23、	将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。

list1 = ['x', 'y', 'z']
list2 = [1, 2, 3]

result = list(zip(list1, list2))
print(result)  # 输出结果：[('x', 1), ('y', 2