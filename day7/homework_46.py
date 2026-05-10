#46、	判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。

set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
has_common_elements = not set1.isdisjoint(set2)
print(has_common_elements)  # 输出结果：True，表示集合 {'A', 'D', 'B'} 和集合 {'D', 'E', 'C'} 中有重复元素 '