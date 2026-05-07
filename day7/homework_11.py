#11、	从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。

list1 = [True, 1, 0, 'x', None, 'x', False, 2, True]
while 'x' in list1:
    list1.remove('x')
print(list1)  # 输出结果：[True, 1, 0, None, False, 2, True]