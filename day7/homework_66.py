#66、	从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。

phone_number = input("请输入手机号码: ")
formatted_number = f"Mobile: {phone_number[:3]} {phone_number[3:7]} {phone_number[7:]}"
print(formatted_number)  # 输出结果：Mobile: 186 6677 7788（假设输入的手机号码是18666777788)


