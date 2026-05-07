#1、把今天讲的列表，元组，字典，字符串的所有接口基本功能练习一遍，并用思维导出总结好
#（不清楚哪些是基础功能，就是照着上课代码练习一遍）

# 1. 列表（List）
list = [1, 2, 3, 4, 5]
# 增加元素
list.append(6)
print(list)  # [1, 2, 3, 4, 5, 6]
list.extend([7, 8])
print(list)  # [1, 2, 3, 4, 5]
list.insert(0, 0)
print(list)  # [0, 1, 2, 3, 4]
print("-----------------------------")
# 删除元素
list = [0, 1, 2, 3, 4, 5]
list.remove(0)
print(list)  # [1, 2, 3, 4, 5]
val = list.pop(1)
print(val)  # 2
print(list)  # [1, 3, 4, 5]
list.clear()
print(list)  # []
print("-----------------------------")
# 查询与统计
list = [1, 2, 3, 4, 5]
index = list.index(3)
print(index)  # 2
count = list.count(2)
print(count)  # 1
length = len(list)
print(length)  # 5
print("-----------------------------")
# 排序与反转
list = [5, 2, 3, 1, 4]
list.sort()
print(list)  # [1, 2, 3, 4, 5]
list.reverse()
print(list)  # [5, 4, 3, 2, 1]
print("-----------------------------")
# 复制
list = [1, 2, 3, 4, 5]
copy_list = list.copy()
print(copy_list)  # [1, 2, 3, 4, 5]'
print("-----------------------------")
# 切片
list = [1, 2, 3, 4, 5]
slice_list = list[1:4]
print(slice_list)  # [2, 3, 4]
print("-----------------------------")

# 2. 元组（Tuple）
# 元组接口与list表相同，但元组是不可变的，所以没有增加、删除、排序等修改操作。

# 3. 字典（Dictionary）

# 创建字典
mydict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(mydict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
mydict = dict(name='Alice', age=30, city='New York')
print(mydict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
mydict = dict.fromkeys(['name', 'age', 'city'], 'unknown')
print(mydict)  # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
print("-----------------------------")

# 访问与获取值

mydict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(mydict['name'])  # Alice
print(mydict.get('age'))  # 30
print(mydict.get('country', 'USA'))  # USA
print(mydict)  # None
print("-----------------------------")

# 增加与修改
mydict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
mydict['age'] = 31
print(mydict)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}
mydict.update({'city': 'Los Angeles'})
print(mydict)  # {'name': 'Alice', 'age': 31,
mydict['country'] = 'USA'
print(mydict)  # {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
print("-----------------------------")

# 删除元素

mydict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
del mydict['age']
print(mydict)  # {'name': 'Alice', 'city': 'New York'}
mydict.pop('city', None)
print(mydict)  # {'name': 'Alice'}
mydict.pop('country', None)  # 不存在的键，返回None
print(mydict)  # {'name': 'Alice'}
mydict.popitem()  # 删除最后一个键值对
print(mydict)  # {}
print("-----------------------------")

# 视图与遍历

mydict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(mydict.keys())  # dict_keys(['name', 'age', 'city'])
print(mydict.values())  # dict_values(['Alice', 30, 'New York'])
print(mydict.items())  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
for key in mydict:
    print(key)  # name age city
for value in mydict.values():
    print(value)  # Alice 30 New York
for key, value in mydict.items():
    print(f"{key}: {value}")  # name: Alice age: 30 city: New York
print("-----------------------------")

# 4. 字符串（String
# 查找与统计

str = "Hello, World!"
index = str.find('o')
print(index)  # 4
index = str.rfind('o')
print(index)  # 8
index = str.index('W')
print(index)  # 7
count = str.count('o')
print(count)  # 2
print("-----------------------------")

# 判断
str = "Hello, World!"
print(str.isalpha())  # False
print(str.isdigit())  # False
print(str.isalnum())  # False
print(str.islower())  # False
print(str.isupper())  # False
print(str.isspace())  # False
print(str.startswith('Hello'))  # True
print(str.endswith('!'))  # True
print("-----------------------------")

# 大小写转换
str = "Hello, World!"
print(str.upper())  # HELLO, WORLD!
print(str.lower())  # hello, world!
print(str.title())  # Hello, World!
print(str.capitalize())  # Hello, world!
print(str.swapcase())  # hELLO, wORLD!
print("-----------------------------")

# 去除空白
str = "   Hello, World!   "
print(str.strip())  # "Hello, World!"
print(str.lstrip())  # "Hello, World!   "
print(str.rstrip())  # "   Hello, World!"
print("-----------------------------")

# 分割与连接
str = "Hello, World!"
parts = str.split(', ')
print(parts)  # ['Hello', 'World!']
parts = str.rsplit(', ', 1)  # 从右侧分割
print(parts)  # ['Hello', 'World!']
parts = str.partition(', ')  # 分割成三部分
print(parts)  # ('Hello', ', ', 'World!')
str = ' '.join(['Hello', 'World!'])  # 连接字符串
print(str)  # Hello, World!
print("-----------------------------")

# 替换与填充
str = "Hello, World!"
new_str = str.replace('World', 'Python')
print(new_str)  # Hello, Python!
str = "123"
new_str = str.zfill(5)  # 在左侧填充0，使长度为5
print(new_str)  # 00123
str = "abc"
new_str = str.center(10, '*')  # 在两侧填充*，使字符串居中，长度为10
print(new_str)  # ***abc****
new_str = str.ljust(10, '-')  # 在右侧填充-，使字符串左对齐，长度为10
print(new_str)  # abc-------
new_str = str.rjust(10, '-')  # 在左侧填充-，使字符串右对齐，长度为10
print(new_str)  # -------abc
print("-----------------------------")

# 格式化
name = "Alice"
age = 30
city = "New York"
str = "My name is {}, I am {} years old, and I live in {}.".format(name, age, city)
print(str)  # My name is Alice, I am 30 years old, and I
str = f"My name is {name}, I am {age} years old, and I live in {city}."
print(str)  # My name is Alice, I am 30 years old, and I live in New York.
print("-----------------------------")


