#67、	从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串。

year = input("请输入年份: ")
month = input("请输入月份: ")
day = input("请输入日期: ")
hour = input("请输入小时: ")
minute = input("请输入分钟: ")
second = input("请输入秒钟: ")
formatted_datetime = f"{year}-{month.zfill(2)}-{day.zfill(2)} {hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}"
print("格式化后的日期时间字符串:", formatted_datetime)  # 输出结果：格式化后的日期时间字符串: '2019-05-01 12:00:00'（