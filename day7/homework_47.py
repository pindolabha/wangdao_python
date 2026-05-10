#47、	判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。

set1 = {'A', 'C'}
set2 = {'D', 'C', 'E', 'A'}
is_subset = set1.issubset(set2)
print(is_subset)  # 输出结果：True，表示集合 {'A', 'C'} 是集合 {'D', 'C', 'E', 'A'} 的子集