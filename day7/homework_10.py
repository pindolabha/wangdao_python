#10、	分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
list1 = [True, False, 0, 1, 2]
count_true = list1.count(True)
count_false = list1.count(False)
count_zero = list1.count(0)
count_one = list1.count(1)
count_two = list1.count(2)
print(f"True的个数：{count_true}")
print(f"False的个数：{count_false}")
print(f"0的个数：{count_zero}")
print(f"1的个数：{count_one}")
print(f"2的个数：{count_two}")
# 发现了什么？
# True和1是等价的，False和0是等价的