# print 99 multiplication table
start = 1

while start < 10:
    for num in range(1, start + 1):
        print(f"{num} x {start} = {num * start}", end=" ")
    print()
    start +=1


# Guess the size of the number
# num = 3
# while True:
#     enter_num = int(input("enter number: "))
#     if enter_num > num:
#         print("too big")
#         continue
#     if enter_num < num:
#         print("too small")
#         continue
#     print("good job")
#     break


# Traverse the list
list_tmp = [1, 2, 3, 4, 5, 6]
for value in list_tmp:
    print(value)

# Traverse the set
set_tmp = {1,3,5}
for value in set_tmp:
    print(value)

# find max number
tmp_num = list_tmp[0]
for value in list_tmp:
    if tmp_num < value:
        tmp_num = value;
else:
    print(tmp_num)

# list slice list[start:end:step] 
# start default is 0
# end default is end number
# step default is 1
list_slice_tmp = list_tmp[1:4:2]
print(list_slice_tmp)


# merge lists
# unpack lists into a new list [*list, *list2]
# merge lists using +   list1 + list2....
print([*list_tmp, *list_slice_tmp])
print(list_tmp + list_slice_tmp)

# list comprehension
# [expression for item in iterable]
list_comperhension = [i**2 for i in range(1,6)]
print(list_comperhension)
# [expression for item in iterable if bool]
list_comperhension2 = [i for i in range(1,11) if i % 2 == 0]
print(list_comperhension2)


# tuple
# packing
t1 = (1,2,3,4)
t2 = 1,2,3,4

# unpacking
a, b, c, d = t1

# extended unpacking
x, *y, z = t1


# set
s1 = {1,6,3}
s2 = {1,9,8}

s3 = s1.difference(s2)
print(s3)
