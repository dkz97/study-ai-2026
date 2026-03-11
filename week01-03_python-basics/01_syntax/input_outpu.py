# 输入函数 input("(提示语）")
name = input("Please input your name: ")
if not name:
    print("Name cannot be empty, Exit program")
    exit()
print(f"welcome {name}!")

age = input ("Please input your age: ")
if not age:
    print("Age cannot be empty, Exit program")
    exit()
print(f"your age is {age}")



# ATM取款
bank_balance = 10000

withdrawal = input("Enter withdrawal amount: ").strip()


if not withdrawal:
    print("Amount cannot be empty. exit program")
    exit()

try:
    float(withdrawal)
except:
    print("Please enter a number")
    exit()

if float(withdrawal) > bank_balance:
    print("Insufficient balance")
    exit()

print(f"Remaining balance: {bank_balance - float(withdrawal)}")