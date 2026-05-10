#69、	将 0.00774592 和 356800000 格式化输出为科学计数法字符串。

num1 = 0.00774592
num2 = 356800000
formatted_str1 = f"{num1:.2e}"
formatted_str2 = f"{num2:.2e}"
print(f"科学计数法字符串: {formatted_str1}, {formatted_str2}")  # 输出结果：科学计数法字符串: 7.75e-03, 3.57e+08