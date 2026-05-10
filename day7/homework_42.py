#42、	返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。

set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
difference = set1 - set2
print(difference)  # 输出结果：{'A', 'B'}，表示集合 {'A', 'B'} 中的元素未出现在集合 {'D', 'E', 'C