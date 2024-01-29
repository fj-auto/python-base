## language type #解释型

解释型语言是那些不需要将程序代码（源代码）完全转换成机器语言的编程语言。相反，它们通常在程序运行时通过一个解释器逐行解释和执行代码。

**编译型语言的特点**

**实时过程**
当你运行一个 Python 程序时，Python 解释器会实时地逐行解释这些代码，将它们转换为可以执行的操作。

当您运行一个 Python 程序时，发生的事情并不是将整个代码转换成二进制代码，而是通过以下步骤：

- 解释过程（Python 解释器逐行读取源代码）
- 字节码转换（首先将 Python 代码转换成一种中间形式，称为字节码（bytecode）。这种字节码是一种低级的、与平台无关的代码表示。）
- Python 解释器（或更准确地说是 Python 虚拟机）随后执行这些字节码。虚拟机是解释字节码并将其转换为特定于操作系统和硬件的操作的组件。

**跨平台性**
通常不依赖于特定的操作系统或硬件。这意味着相同的 Python 代码可以在不同的平台上运行，只要那些平台上安装了 Python 解释器。

**性能**
解释型语言通常比编译型语言执行速度慢，因为代码在运行时需要实时解释。但是，这也为动态类型检查、即时错误报告和其他灵活性提供了空间。

**错误检测**
很多错误（如运行时错误）会在代码实际执行到那一行时才被检测到。

**即时编写和测试**
解释型语言允许开发者即时编写和测试代码片段，而无需整个程序的编译过程。

**依赖解释器**
解释型语言的程序依赖于解释器。这意味着要运行 Python 程序，目标机器上必须安装 Python 解释器。

## 静态类型 vs 动态类型

#### 静态类型语言 - GoLang

在静态类型语言中，变量的类型在编译时就已经明确确定，并且在整个程序运行过程中不会改变。

**类型检查**
在编译时进行类型检查。这意味着你必须在编写代码时指定每个变量的类型，编译器会在编译过程中检查类型的正确性。

**错误检测**
这种早期类型检查有助于在代码运行之前发现错误，例如类型不匹配的错误。

**性能**
静态类型有助于优化性能。因为编译器知道每个变量的确切类型，它可以生成更有效的机器代码。

**代码清晰性**
静态类型通常要求更明确的代码结构，这使得代码更易于理解和维护。

#### 动态类型语言 - Python

动态类型语言允许变量在运行时改变其类型。

**运行时类型确定**
变量的类型是在运行时确定的。你可以在程序执行的过程中改变变量的类型。

**灵活性**
这种动态类型提供了更大的灵活性。程序员可以编写更加通用和灵活的代码。

**易用性**
对于初学者和快速原型开发来说，动态类型系统通常更加容易使用。

**运行时错误**
类型错误可能只有在实际执行到相关代码时才会被发现，这可能会导致运行时错误。

#### 总结

**静态类型**：类型在编译时确定，不可更改。这有助于早期错误检测和性能优化。
**动态类型**：类型在运行时确定，并且可以更改。这提供了灵活性和易用性，但可能导致运行时错误。

## variables

变量赋值这个过程不需要显式声明变量的类型，因为 Python 是一种动态类型语言。你不需要声明变量的类型；它是在赋值时自动确定的。

命名规则，例如，它们不能以数字开头，不能包含特殊字符（除了下划线\_），不能是 Python 的保留关键字，等等。

变量可以在程序的任何地方被重新赋值，甚至可以改变它们的类型。

**基本赋值**

```py
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
```

**多重赋值/同为为多个变量赋值 multiple assignment**

```py
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

```

**链式赋值 chained assignment**

```py
a = b = c = 10
print(a)
print(b)
print(c)
```

**重新赋值 reassignment**

```py
a = 10
print(a)
a = 20
print(a)
```

**类型检查**
在 Python 中，一切都是对象，包括基本数据类型如整数、浮点数、字符串等。这意味着即使是这些基本数据类型也有与之关联的类和属性。当你创建一个整数时，你实际上是创建了 `int` 类的一个实例。

在 Python 这样的动态类型语言中，虽然不需要在定义变量时指定其类型，但有时候我们需要在程序运行时检查变量的类型。

- 使用 `type()` 适用于直接检查对象的类型。

```py
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
```

- 使用 `isinstance()` 更适合检查一个对象是否是一个给定类或其子类的实例。这个函数在处理继承时特别有用，因为它会考虑到继承层次结构。

```py
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
```

> 基础数据类型也可以使用 `isinstance()` 进行检查。返回值是布尔值 `True` 或 `False`。
> 在实际编程中，通常更推荐使用 isinstance()，因为它在面向对象编程中更加灵活。

**隐式/显式类型转换**

在 Python 中，类型转换可以是显式的或隐式的。显式类型转换是程序员明确进行的，而隐式类型转换是由 Python 自动进行的。

- 显式类型转换（显式类型转换通常通过调用 Python 内置的函数来实现。）

```py
number = int("123") # 字符串到整数

number = float("3.14") # 字符串到浮点数

text = str(123) # 整数到字符串

my_list = list("Hello") # 字符串到列表，结果是 ['H', 'e', 'l', 'l', 'o']

my_tuple = tuple([1, 2, 3]) # 列表到元组，结果是 (1, 2, 3)

my_set = set([1, 2, 3]) # 列表到集合，结果是 {1, 2, 3}

my_dict = dict([("name", "John"), ("age", 20)]) # 列表到字典，结果是 {"name": "John", "age": 20}

boolean = bool(1) # 任何非零数到布尔值，结果是 True
```

- 隐式类型转换（隐式类型转换是由 Python 自动进行的，不需要程序员的干预。这通常发生在 Python 需要自动协调两种不同类型的数据时。）

**算术运算中的类型提升**
当对不同类型的数字进行算术运算时，Python 会自动将较“小”的类型（如整数）转换为较“大”的类型（如浮点数）。

```py
result = 3 + 2.5  # 整数和浮点数的加法，3自动转换为浮点数
```

**布尔运算**
在布尔上下文中（如 if 语句），非布尔类型的值会被隐式转换为布尔值。

```py
if "hello":  # 字符串在布尔上下文中隐式转换为 True
    print("String is truthy")
```

**字符串连接**
当使用加号（+）将字符串和非字符串值连接时，非字符串值会被隐式转换为字符串（这种做法通常不推荐，因为可能会引起错误）。

```py
greeting = "Hello, " + str(123)  # 数字123被显式转换为字符串

# 这种做法通常不推荐，因为可能会引起错误
result = 3 + 2.5
print(result)  # 输出 5.5
# 3 被隐式转换为浮点数 3.0，然后与 2.5 相加
```

**隐式类型转换的情况，包括那些可能导致错误或混淆的场景。**

- 数值运算中的隐式类型转换

```py
# 整数与浮点数的运算：
result = 3 + 2.5
print(result)  # 输出 5.5
# 3 被隐式转换为浮点数 3.0，然后与 2.5 相加

# 布尔值与数字的运算：
result = True + 5
print(result)  # 输出 6
# True 被隐式转换为 1
```

- 逻辑运算中的隐式类型转换

```py
# 布尔上下文中的非布尔值：
if "hello":
    print("Non-empty string is truthy")
# 非空字符串在布尔上下文中被隐式视为 True

# 空列表在布尔上下文中的转换：
if []:
    print("This won't print")
else:
    print("Empty list is falsy")
# 空列表 [] 被隐式视为 False
```

- 字符串连接中的隐式转换

```py
# 字符串与数值的连接（不推荐，易引起错误）：
# 这将引发错误，因为无法将整数直接与字符串相连
# text = "The number is " + 5

# 正确的做法是显式转换
text = "The number is " + str(5)
print(text)  # 输出 "The number is 5"
```

- 潜在的混淆或错误

```py
# 不同类型的比较：
# 尽管这在Python中是合法的，但可能导致混淆
result = "5" == 5
print(result)  # 输出 False
# 字符串 "5" 和整数 5 不是相同的

# 列表加法与整数（不合法，会引发错误）：
# 这将引发TypeError，因为列表和整数无法相加
# result = [1, 2, 3] + 5
```

**变量的作用域**
在讨论变量的作用域时，确实需要考虑变量在程序中的可见性和可访问性。

- 局部作用域（Local）：在函数内定义的变量具有局部作用域。这些变量只在定义它们的函数内部可见和可用

```py
# 局部作用域 local scope（局部变量 local variable）
def local_scope_example():
    local_var = "I am a local variable"
    print(local_var) # 正确访问

local_scope_example()
print(local_var) # 会引发错误，因为local_var在此作用域外不可见

# 在这个例子中，local_var 在 local_scope_example 函数内定义，因此只能在这个函数内部被访问。
```

- 封闭作用域（Enclosing）：在嵌套函数中，外部函数的作用域被称为封闭作用域。一个封闭作用域的变量对内部函数是可见的，但只有在没有同名局部变量的情况下。

```py
# 封闭作用域 enclosing scope（外部变量 enclosing variable）
def outer_function():
    enclosing_val = "I am an enclosing variable"

    def inner_function():
        print(enclosing_val) # 可以访问外层函数的变量

    inner_function()

outer_function()

# 在这个例子中，enclosing_var 是在 outer_function 函数内定义的，它在嵌套的 inner_function 内是可见的。
```

- 全局作用域（Global）：在程序最顶层定义的变量具有全局作用域。这些变量在整个文件的任何地方都是可见和可用的。

```py
# 全局作用域 global scope（全局变量 global variable）
global_var = "I am a global variable"

def global_scope_example():
    print(global_var) # 可以访问全局变量

global_scope_example()
print(global_var) # 在函数外也可以访问

# 在这个例子中，global_var 是全局定义的，因此可以在函数内外被访问。

# 全局变量的修改
# 在函数内部修改全局变量时，需要使用 global 关键字。
global_var = "I am a global variable"

def modify_global_var():
    global global_var
    global_var = "I am a modified global variable"

modify_global_var()
print(global_var) # 输出 I am a modified global variable

# 在这个例子中，我们在 modify_global_var 函数中修改了全局变量 global_var 的值。使用 global 关键字可以确保我们修改的是全局作用域中的变量。
```

- 内建作用域（Built-in）：Python 自身定义的变量，如函数 print()和 len()，存在于内建作用域中。

```py
# 内置作用域 built-in scope（内置变量 built-in variable）
print(len("I am using a built-in function")) # len 是一个内建函数

# 在这个例子中，len 是Python的内建函数，可以在任何地方使用，无需特别声明。
```

Data Types

- **基本数据类型**
- **Python**:
  - 数值：int, float, complex
  - 字符串：str
  - 布尔值：bool (True, False)
- **Go**:
  - 数值：int, int8, int16, int32, int64, uint, uint8 (byte), uint16, uint32, uint64, uintptr, float32, float64, complex64, complex128
  - 字符串：string
  - 布尔值：bool (true, false)
- **JavaScript**:
  - 数值：Number (包括整数和浮点数)
  - 字符串：String
  - 布尔值：Boolean (true, false)
  - Undefined 和 Null 类型
- **复合数据类型**
  - **Python**: list, tuple, set, dict
  - **Go**: array, slice, struct, map, channel, interface
  - **JavaScript**: Array, Object, Set, Map, WeakSet, WeakMap, Date
- **特殊数据类型**
  - **Python**: NoneType (None)
  - **Go**: 函数类型, 指针类型, 接口类型
  - **JavaScript**: Function, Symbol, BigInt

Operators

- **算术操作符**
  - **Python/Go/JavaScript**: `+`, `-`, `*`, `/`, `%` (取余)
  - **Go/JavaScript**: `++` (自增), `--` (自减)
  - **Python**: `//` (整除), `**` (幂)
- **比较操作符**
  - **Python/Go/JavaScript**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **逻辑操作符**
  - **Python**: `and`, `or`, `not`
  - **Go/JavaScript**: `&&`, `||`, `!`
- **位操作符**
  - **Python/Go/JavaScript**: `&`, `|`, `^`, `~`, `<<`, `>>`
  - **Go/JavaScript**: `&^` (位清除)
- **赋值操作符**
  - **Python/Go/JavaScript**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
  - **Go/JavaScript**: `&=`, `|=`, `^=`, `<<=`, `>>=`, `&^=`
- **特殊操作符**
  - **Python**: `is`, `is not`, `in`, `not in`
  - **Go**: `<-` (用于 channels)
  - **JavaScript**: `typeof`, `instanceof`, `new`, `in`, `delete`, `=>` (箭头函数)

Data Structures in language

- **列表/数组**
  - **Python**: List (`list`) 是 Python 中的动态数组，可以包含不同类型的元素。
  - **Go**: Slice（`[]Type`）是 Go 中的动态数组，但它要求所有元素都是相同的类型。Go 也有 Array（`[N]Type`），但它的大小是固定的。
  - **JavaScript**: Array (`Array`) 是 JavaScript 中的动态数组，它可以容纳不同类型的元素，并且大小是可以变化的。
- **不可变序列/元组**
  - **Python**: Tuple (`tuple`) 是一个不可变的序列，可以包含不同类型的元素。
  - **Go**: Go 没有直接等价于 tuple 的类型。最接近的可能是使用 Array 或 Struct。Struct 可以包含不同类型的数据。
  - **JavaScript**: JavaScript 没有原生的 tuple 类型。但可以使用 Array 来模拟（虽然它是可变的），或者使用第三方库提供的 tuple 实现。
- **字典/映射**
  - **Python**: Dictionary (`dict`) 是一个键值对集合，其中的键和值可以是不同类型。
  - **Go**: Map (`map[KeyType]ValueType`) 是键值对的集合，要求所有的键是相同类型，所有的值也是相同类型。
  - **JavaScript**: Object (`Object`) 通常用作键值对的集合。ES6 引入了 Map 对象，提供了更完整的映射功能。
- **集合**
  - **Python**: Set (`set`) 是一个无序且元素不重复的集合。
  - **Go**: Go 没有内建的 set 类型，但可以通过使用 map（通常是 `map[ElementType]bool`）来模拟。
  - **JavaScript**: ES6 引入了 Set (`Set`) 类型，它是一个无序且元素不重复的集合。

Control Flow

- **条件语句**（`if`, `else`, `else if`）
- **循环**（`for`, `while`, `do...while`）
- **跳转语句**（`break`, `continue`, `return`）
- **Switch 语句**（`switch`, `case`, `default`）
- **异常处理**（`try`, `catch`, `finally`, `throw`）

Procedure
通常指的是一段执行特定任务的代码。它类似于函数，但在某些编程语言和上下文中，通常与不返回值的函数相关联，或者更侧重于执行一系列操作而非计算并返回值。

Functions

### Python 中的函数

1. **定义**：使用 `def` 关键字定义函数。

   `def my_function(param1, param2):     return param1 + param2`

2. **动态类型**：参数和返回值可以是任何类型，不需要显式声明。

3. **默认参数和可变参数**：支持默认参数值，以及可变数量的参数。

4. **一等公民**：函数是一等公民，可以作为参数传递，赋值给变量，从其他函数返回。

5. **匿名函数**：通过 `lambda` 关键字支持匿名函数（通常用于简单的操作）。

### Go 中的函数

1. **定义**：使用 `func` 关键字定义函数。需要显式声明参数类型和返回值类型。

   `func myFunction(param1 int, param2 int) int {     return param1 + param2 }`

2. **静态类型**：函数的参数和返回值必须明确其类型。

3. **多返回值**：支持返回多个值。

4. **一等公民**：和 Python 类似，Go 的函数也是一等公民。

5. **匿名函数和闭包**：支持匿名函数和闭包。

### JavaScript 中的函数

1. **定义**：使用 `function` 关键字或箭头函数（`=>`）定义函数。

   `function myFunction(param1, param2) {     return param1 + param2; }  // 箭头函数 const myFunction = (param1, param2) => param1 + param2;`

2. **动态类型**：参数和返回值可以是任何类型，JavaScript 是一种动态类型语言。

3. **一等公民**：函数在 JavaScript 中也是一等公民。

4. **函数提升（Hoisting）**：函数声明在编译时被提升到顶部，允许在声明前调用函数。

5. **匿名函数和闭包**：广泛使用匿名函数和闭包。

Abstraction
是一个非常核心的概念，它指的是简化复杂的现实世界问题，通过隐藏复杂的细节，只展示对用户或程序员重要的信息。这种方法使得程序员可以专注于高级操作，而不必关心底层的细节实现。
通常是，通过类（classes）和函数（functions）来实现

- 在 Python 中，抽象可以通过类（classes）和函数（functions）来实现。
- 在 Go 中，抽象同样可以通过结构体（structs）和接口（interfaces）来实现。
- JavaScript 通过对象和函数来实现抽象。你可以使用对象来封装属性和方法。

一等公民（First-Class Citizen）
实体具有以下几个特征：

1. **可以存储在变量中**：实体可以被赋值给一个变量。
2. **可以作为参数传递**：实体可以作为函数的参数。
3. **可以作为返回值**：实体可以作为函数的返回值。
4. **可以在运行时创建**：实体可以在程序运行时动态创建，而不仅仅在编译时确定。
   `function greet(name) {`
   `return "Hello, " + name;`
   `}`

`// 将函数存储在变量中`
`var sayHello = greet;`

`// 将函数作为参数传递`
`function greetLoudly(func, name) {`
`var greeting = func(name);`
`console.log(greeting.toUpperCase());`
`}`

`greetLoudly(sayHello, "Alice");`

`// 函数作为返回值`
`function getGreetingFunction() {`
`return greet;`
`}`

`var greetFunc = getGreetingFunction();`
`console.log(greetFunc("Bob"));`

柯里化（Currying）
是一个在函数式编程中常见的概念，它指的是将一个多参数的函数转换成多个单参数（或较少参数）的函数的过程。这样做的目的是为了减少函数调用所需的参数数量，通过固定一些参数来创建一个新的函数。

代码组织
