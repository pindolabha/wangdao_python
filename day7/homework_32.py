#32、	以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，
# 创建一个字典。
keys_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
mydict = dict.fromkeys(keys_list, 0)
print(mydict)  # 输出结果：{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}