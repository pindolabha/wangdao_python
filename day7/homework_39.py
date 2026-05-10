#39、	返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。

my_tuple = (2, 5, 3, 7)
# 将元组转换为列表以便插入元素
temp_list = list(my_tuple)
# 在索引号为2的位置插入元素9
temp_list.insert(2, 9)
# 将列表转换回元组
new_tuple = tuple(temp_list)
print(new_tuple)  # 输出结果：(2, 5, 9, 3, 7)