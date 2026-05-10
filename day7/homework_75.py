#75、	将等长的键列表和值列表转为字典。

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
result_dict = dict(zip(keys, values))
print(result_dict)  # 输出结果：{'name': 'Alice', 'age': 30, 'city': 'New York'}，表示将等长的键列表和值列表