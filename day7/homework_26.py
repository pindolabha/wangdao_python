#26、	以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。

mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
items_list = list(mydict.items())
print(items_list)  # 输出结果：[('Alice', 20), ('Beth', 18), ('Cecil', 21)]