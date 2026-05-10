#44、	返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。

set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
intersection = set1 & set2
print(intersection)  # 输出结果：{'D'}，表示集合 {'D'} 中的元素同时出现在集合 {'A', 'D', 'B'} 和集合 {'D',