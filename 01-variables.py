# 为整数赋值
number = 10
print(number)

# 为字符串赋值
text = "Hello World"
print(text)

# 为列表赋值（在JS中称作数组）
fruits = ["apple", "banana", "cherry"]
print(fruits)

# 列表可以包含不同类型的元素
mixed = [10, "Hello World", True]
print(mixed)

# 为字典赋值（在JS中称作对象）
person = {"name": "John", "age": 20}
print(person)

# 字典可以包含不同类型的值
mixed_dict = {"name": "John", "age": 20, "hobbies": ["Reading", "Music"]}
print(mixed_dict)

# 链式赋值 chained assignment
a = b = c = 10
print(a)
print(b)
print(c)

# 多重赋值、同时为多个变量赋值 multiple assignment
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

# 重新赋值 reassignment
a = 10
print(a)
a = 20
print(a)

# 局部作用域 local scope（局部变量 local variable）
def local_scope_example():
    local_var = "I am a local variable"
    print(local_var) # 正确访问

local_scope_example()
# print(local_var) # 会引发错误，因为local_var在此作用域外不可见

# 封闭作用域 enclosing scope（外部变量 enclosing variable）
def outer_function():
    enclosing_val = "I am an enclosing variable"

    def inner_function():
        print(enclosing_val) # 可以访问外层函数的变量

    inner_function()

outer_function()


# 全局作用域 global scope（全局变量 global variable）
global_var = "I am a global variable"

def global_scope_example():
    print(global_var) # 可以访问全局变量

global_scope_example()
print(global_var) # 在函数外也可以访问


# 内置作用域 built-in scope（内置变量 built-in variable）
print(len("I am using a built-in function")) # len 是一个内建函数

# 类型判断 type checking

# type() 函数可以用来判断变量的类型，适用于直接检查对象的类型。

a = 10
print(type(a)) # <class 'int'>

b = "Hello"
print(type(b)) # <class 'str'>

c = [1, 2, 3]
print(type(c)) # <class 'list'>

d = {"name": "John", "age": 20}
print(type(d)) # <class 'dict'>

e = (1, 2, 3)
print(type(e)) # <class 'tuple'>

f = {1, 2, 3}
print(type(f)) # <class 'set'>

g = 3.14
print(type(g)) # <class 'float'>

h = True
print(type(h)) # <class 'bool'>

def function():
    pass
print(type(function)) # <class 'function'>

# 使用 `type()` 来判断变量的类型，需要将该变量的类型与 str 类型直接进行比较
text = "Hello World"
is_string = type(text) == str
print(is_string) # 如果 text 是一个字符串，将输出 True

# isinstance() 用于检查一个对象是否是一个特定类的实例。这个函数在处理继承时特别有用，因为它会考虑到继承层次结构。
a = 10
print(isinstance(a, int)) # True

b = "Hello"
print(isinstance(b, str)) # True

c = [1, 2, 3]
print(isinstance(c, list)) # True

d = {"name": "John", "age": 20}
print(isinstance(d, dict)) # True

e = (1, 2, 3)
print(isinstance(e, tuple)) # True

f = {1, 2, 3}
print(isinstance(f, set)) # True

g = 3.14
print(isinstance(g, float)) # True

h = True
print(isinstance(h, bool)) # True

def function():
    pass
print(isinstance(function, function.__class__)) # True


# 类型转换 type casting
# 显示转换 explicit casting
number = int("123") # 字符串到整数
number = float("3.14") # 字符串到浮点数
text = str(123) # 整数到字符串
my_list = list("Hello") # 字符串到列表，结果是 ['H', 'e', 'l', 'l', 'o']
my_tuple = tuple([1, 2, 3]) # 列表到元组，结果是 (1, 2, 3)
my_set = set([1, 2, 3]) # 列表到集合，结果是 {1, 2, 3}
my_dict = dict([("name", "John"), ("age", 20)]) # 列表到字典，结果是 {"name": "John", "age": 20}
boolean = bool(1) # 任何非零数到布尔值，结果是 True

# 隐式转换 implicit casting