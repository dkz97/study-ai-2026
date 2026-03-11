# for/while

"""
    while 条件表达式:
        循环体语句1
        循环体语句2
        ......
    else(可选):
        循环正常结束时执行的操作
"""
num = 1
while num < 100:
    num += 1
else:
    print("end of loop")
print(num)


# print number from 1 to 100
num = 1
while num <= 100:
    print(num)
    num += 1

# print even numbers from 1 - 100
num = 1
while num <= 100:
    if (num % 2 == 0):
        print(num)
    num += 1


# Sum number from 1 to 100
num = 1
result = 0
while num <= 100:
    result += num
    num += 1
print(result)


# Sum even numbers from 1 to 100
num = 1
result = 0
while num <= 100:
    if (num % 2 ==0):
        result += num
    num += 1
print(result)


"""
    for 元素 in 待处理数据集:
        循环体代码
    else(可选):
        循环正常结束时，执行的代码
"""
msg = "Hello, World"
for s in msg:
    print(s)


list_tmp = ["a", 1, "damn"]
for value in list_tmp:
    print(value)


"""
    while: 用于在某个条件满足时一直进行的循环，循环次数通常未知，关注的是循环的条件
    for: 用于对一个已知的数据集进行遍历或已知次数的循环，关注的是遍历每一个元素
    range(): 生成制定规则的数字序列
"""
range_tmp_1 = range(5)
for v in range_tmp_1:
    print(v)

range_tmp_2 = range(1,10)
for v in range_tmp_2:
    print(v)

range_tmp_3 = range(1,10,2)
for v in range_tmp_3:
    print(v)