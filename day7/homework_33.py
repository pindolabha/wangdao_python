#33、	将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
list_of_pairs = [['a', 1], ['b', 2]]
tuple_of_pairs = (('x', 3), ('y', 4)) 
dict_from_list = dict(list_of_pairs)
dict_from_tuple = dict(tuple_of_pairs)
print(dict_from_list)  # 输出结果：{'a': 1, 'b': 2}
print(dict_from_tuple)  # 输出结果：{'x': 3, '