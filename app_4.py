print("return.............")
def double_num(num):
    print(1)
    return num*2
new_num = double_num(10)
print(new_num)
print("if.............")

is_hot = True
is_cold = True
if is_hot:
    print("天气很热")
    print("需要多喝水")
elif is_cold:
    print("天气很冷")
    print("需要穿很多衣服")
else:
    print("天气很舒服")
# 按 shift+tab 键 取消缩进
print("好好享受这一天")
# 逻辑运算符 logica operators
print("逻辑运算符...............")
is_good_singer = True
is_good_dancer = True
if is_good_singer and is_good_dancer:
    print("通过测试")

is_good_singer = False
is_good_dancer = True
if is_good_singer or is_good_dancer:
    print("通过测试")
print("not....................")
is_good_singer = True
is_good_dancer = True
has_criminal_record = False
if is_good_singer and not has_criminal_record:
    print("通过测试")

# 比较运算符  comparison operators: > >= <= == !=
# str_age = input("请输入你的年龄：")
str_age=5
age = int(str_age)
if age <= 5:
    print("child")
else:
    print("big man")
print("............")
if age == 5:
    print("child")
else:
    print("big man")

if age != 5:
    print("child")
else:
    print("big man")

# 字典 dictionary dict
# key-value
customer = {
    "nickname":"李四",
    "age":30,
    "is_vip":False,
    2:5
}
# 字典 的访问方式1
print(customer["nickname"])
# print(customer["id"])
# 字典 的访问方式2
print(customer.get("age"))
# 没有返回None,可以指定返回的默认值，如：000000
print(customer.get("id","000000"))
# 更新字典
print(customer["is_vip"])
customer["is_vip"]=True
print(customer["is_vip"])
# 在字典里面添加key-value
customer["id"]="123"
print(customer["id"])

# while
i=1
while i<=8:
    print(i)
    i=i+1
print("结束循环")

i=1
while i<=8:
    # 字符串*数字：表示重复字符串的次数
    print("￥"*i)
    i=i+1
print("结束循环")

# for
# 序列
#interater
# 输出字符串
for item in "i love u":
    print(item)
# 输出列表
for item in ["张山","李四","王五"]:
    print(item)
for item in [1,2,3,4,5]:
    print(item)
print("使用range函数创建整数序列")
# 如下：输出0到9
for item in range(10):
    print(item)
# 输出范围
for item in range(100,110):
    print(item)
# 设置步长2
for item in range(100,110,2):
    print(item)
# 序列式的都可以使用for来迭代：list，tuple，字符串等
# 嵌套循环
print("嵌套循环............................")
num_list1 = [1,2,3,4]
num_list2 = [6,7,8,9]
for item_1 in num_list1:
    for item_2 in num_list2:
        print(f'({item_1},{item_2})')
# 格式化字符串
# msg = f'他是{name},已经{age}公斤了'


# 二位列表
#维度 dimension
# two demension list
# 2D list
# dim
