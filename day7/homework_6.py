#6、	将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。

tuple1 = (1, 2, 3)
set1 = {4, 5, 6}
merged_list = list(tuple1) + list(set1)
print(merged_list)  # [1, 2, 3, 4,