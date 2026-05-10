#57、	将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。

str = '2.72, 5, 7, 3.14'
elements = str.split(',')  # 以半角逗号切片
converted_elements = []
for element in elements:
    element = element.strip()  # 去除元素两端的空格
    if '.' in element:  # 判断是否包含小数点，决定转换成浮点型还是整形
        converted_elements.append(float(element))
    else:
        converted_elements.append(int(element))
print("转换后的元素列表:", converted_elements)  # 输出结果：转换后的元素列表: [2.72, 5, 7, 3.14]