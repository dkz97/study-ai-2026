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