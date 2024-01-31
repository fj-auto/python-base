
# 当 input() 函数被调用时，程序会暂停执行
res =input("Enter your name: ")
print("Hello " + res)

# input() 函数总是返回一个字符串
age = input("Enter your age: ")
print(type(age)) # <class 'str'>
print("You are " + age + " years old")
print("You will be " + str(int(age) + 1) + " next year")