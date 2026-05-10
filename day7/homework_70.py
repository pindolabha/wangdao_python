#70、	将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型。

lst = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
bool_lst = [bool(element) for element in lst]
print(bool_lst)  # 输出结果：[False, True, True, True, True, False, False, False, True]，表示列表中各个元素转换为布尔型