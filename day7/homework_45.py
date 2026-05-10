#45、	返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。

set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # 输出结果：{'A', 'B', 'E', 'C'}，表示集合 {'A', 'B', 'E', 'C'} 中的