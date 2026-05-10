#43、	返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。

set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
union = set1 | set2
print(union)  # 输出结果：{'A', 'D', 'B', 'E', 'C'}，表示集合 {'A', 'D', 'B', 'E',