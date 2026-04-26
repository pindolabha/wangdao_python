def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def div_int(a, b):
    return a // b

def mod(a, b):
    return a % b

def pow(a, b):
    return a ** b

# 闰年
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if __name__ == "__main__":
    print(add(1, 2))
    print(sub(1, 2))
    print(mul(1, 2))
    print(div(5, 2))
    print(div_int(5, 2))
    print(mod(5, 2))
    print(pow(2, 3))
    year = input("请输入一个年份:")
    print("%s年是%s" % (year, "闰年" if is_leap_year(int(year)) else "平年"))