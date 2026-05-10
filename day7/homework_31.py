import copy

#31、	若 a = dict()，令 b = a，执行 b.update({'x':1})， a亦被改变。为何？
# 如何避免？----讲了深COPY和浅COPY再做

a = dict()
b = a
b.update({'x': 1})
print(a)  # 输出结果：{'x': 1}
print(b)  # 输出结果：{'x': 1}

# 避免这种情况的方法是使用 copy 模块中的 deepcopy 函数来创建 a 的一个深复制，

a = dict()
b = copy.deepcopy(a)
b.update({'x': 1})
print(a)  # 输出结果：{}
print(b)  # 输出结果：{'x': 1}
