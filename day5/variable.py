def change_Num(iNum):
    iNum = 20
    print(iNum)

iNum = 10
print(iNum)
change_Num(iNum)

def change_Bool(bRet):
    bRet = False
    print(bRet)

bRet = True
change_Bool(bRet)

list = [1, 2, 3, 4, 5]
print(list)
def change_List(list):
    list.append(6)
    list.pop(0)
    list[0] = 100
    print(list)

change_List(list)

set = {1, 2, 3, 4, 5}
print(set)
def change_Set(set):
    set.add(6)
    set.remove(1)
    print(set)

change_Set(set)

dict = {"name": "John", "age": 20}
print(dict)
def change_Dict(dict):
    dict["name"] = "Tom"
    dict["age"] = 21
    print(dict)

change_Dict(dict)

tuple = (1, 2, 3, 4, 5)
print(tuple)
def change_Tuple(tuple):
    # tuple.append(6)
    # tuple.pop(0)
    # tuple[0] = 100
    print(tuple)

change_Tuple(tuple)
