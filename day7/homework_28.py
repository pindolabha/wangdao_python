#28、	删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
del mydict['Beth']  # 删除 'Beth' 键
print(mydict)  # 输出结果：{'Alice': 20, 'Cecil': 21}
mydict.clear()  # 清空字典
print(mydict)  # 输出结果：{}