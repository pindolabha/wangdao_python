#60、	清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。

str = '\t python \n'
left_stripped = str.lstrip()
right_stripped = str.rstrip()
fully_stripped = str.strip()    
print("左侧空白字符被清除:", repr(left_stripped))  # 输出结果：左侧空白字符被清除: 'python \n'
print("右侧空白字符被清除:", repr(right_stripped))  # 输出结果：右侧空白字符被清除: '\t python'
print("左右两侧空白字符被清除:", repr(fully_stripped))  # 输出结果：左右两侧空白字符被清除: 'python'