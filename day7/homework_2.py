#2、	编写代码理解 局部变量与全局变量

# 全局变量
global global_var
global_var = "I am a global variable"

def modify_variables(local_var):
    # 局部变量
    local_var = "modify local variable"
    global global_var
    global_var = "modify global variable"

def test_variables():
    print(global_var)  # I am a global variable
    local_var = "I am a local variable"
    print(local_var)  # I am a local variable
    modify_variables(local_var)
    print(global_var)  # I am a global variable
    print(local_var)  # I am a local variable

test_variables()