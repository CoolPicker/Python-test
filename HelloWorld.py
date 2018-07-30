# 当行注释由一个 # 号开头
"""
    三个双引号(或单引号)之间可以写多行字符串，
    通常用来写注释。
"""

# 1. 基本数据类型和操作符
# 数字就是数字
3
# 四则运算
1 + 1
2 - 1
10 * 2
35 / 5
print(5/3)
# 浮点数
# 可以使用小括号来强制计算的优先顺序

# 布尔值也是基本数据类型 使用not来取反
print(not True)

# 等式判断用 == 更多 != > < >= <=
print(1 < 2 < 3) # 比较运算符可连接

# 使用""或'' 来创建字符串 用 + 做字符串的连接
print('Hello' + ' World')

# 一个字符串可以视为一个字符的列表
print('ABCDEFG'[2])

# % 可以用来格式化字符串
print("%s can be %s" % ("strings","interpolated"))

# 推荐 格式化字符串
print("{0} can be {1}".format("string1","string2"))
print("{0} can be {2}".format("string1","string2","string3"))

#不喜欢数数，可以使用关键字（变量）
print("{name} can be {color}".format(name="tom",age="14",food="dumplings",color="yellow"))

'''
None 是一个对象
不要使用 '==' 比较对象和None,而要用 is
is 操作符用于比较两个对象的标识。
（对象一旦建立，其标识就不会改变，可认为是对象的内存地址。）
处理基本数据类型基本无用，常用于处理对象
'''
print("etc" is None)
print(None is None)

# None、0以及空字符串和空列表都等于False，除此之外的所有值都能与true
0 == False

####################################################
## 2. Variables and Collections
## 2. 变量和集合
####################################################

# 在赋值给变量之前不需要声明
# 变量名的约定是使用下划线分隔的小写字母
some_var = 5
print(some_var)

# if 可以作为表达式来使用
print("Hello World") if some_var>4 else 2

# 列表用于存储序列
li = []
other_li = [1,2,3]
# 使用append方法把元素添加到列表的尾部
li.append(1)
li.append(2)
li.append(3)
li.append(5)
li.append(4)
print(li)
# 使用pop方法来移除最后一个元素
li.pop()
print(li)
# 访问列表，0-正数，从前之后，负数从后向前，越界查询报索引错误
print(li[-1])
# 使用切片语法来查询列表的范围（范围相当于数学中的左闭右开区间）
print(li[1:3])
print(li[:2])
print(li[2:])
# 使用del来删除列表中的任意元素
del li[2]
print(li)
# 可以把列表相加
print(li + other_li)
# 使用extend来合并列表
li.extend(other_li)
print(li)
# 用 in 来检查是否存在于某个列表中
1 in li
# 用 len 来检查列表的长度
print(len(li))

# 元组很像列表，但它是“不可变”的 不能直接赋值
tup = (1,2,3)
tup[0]
# 操作列表的方式也能用在元组身上
len(tup)
tup + (4,5,6)
tup[:3]
3 in tup
# 可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1,2,3)
# 如果省去了小括号，那么元组会自动创建
d, e, f = 4,5,6
# 交换两个值，很简单
e, d = d, e

# 字典用于存储映射关系
empty_dict = {}
# 一个预填充的字典
filled_dict = {"one":1,"two":2,"three":3}
# Look up values with []
# 使用 [] 来查询键值
filled_dict["one"]  # => 1

# Get all keys as a list
# 将字典的所有键名获取为一个列表
filled_dict.keys()  # => ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致。

# Get all values as a list
# 将字典的所有键值获取为一个列表
filled_dict.values()  # => [3, 2, 1]
# Note - Same as above regarding key ordering.
# 请注意：顺序的问题和上面一样。

# Check for existence of keys in a dictionary with in
# 使用 in 来检查一个字典是否包含某个键名
"one" in filled_dict  # => True
1 in filled_dict  # => False

# Looking up a non-existing key is a KeyError
# 查询一个不存在的键名会产生一个键名错误
filled_dict["four"]  # KeyError
# 键名错误

# Use get method to avoid the KeyError
# 所以要使用 get 方法来避免键名错误
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# The get method supports a default argument when the value is missing
# get 方法支持传入一个默认值参数，将在取不到值时返回。
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4

# Setdefault method is a safe way to add new key-value pair into dictionary
# Setdefault 方法可以安全地把新的名值对添加到字典里
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
# filled_dict["five"] 被设置为 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5
# filled_dict["five"] 仍然为 5


# Sets store ... well sets
# set 用于保存集合
empty_set = set()
# Initialize a set with a bunch of values
# 使用一堆值来初始化一个集合
some_set = set([1, 2, 2, 3, 4])  # some_set is now set([1, 2, 3, 4])
# some_set 现在是 set([1, 2, 3, 4])

# Since Python 2.7, {} can be used to declare a set
# 从 Python 2.7 开始，{} 可以用来声明一个集合
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}
# （译注：集合是种无序不重复的元素集，因此重复的 2 被滤除了。）
# （译注：{} 不会创建一个空集合，只会创建一个空字典。）

# Add more items to a set
# 把更多的元素添加进一个集合
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# filled_set 现在是 {1, 2, 3, 4, 5}

# Do set intersection with &
# 使用 & 来获取交集
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Do set union with |
# 使用 | 来获取并集
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
# 使用 - 来获取补集
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Check for existence in a set with in
# 使用 in 来检查是否存在于某个集合中
2 in filled_set  # => True
10 in filled_set  # => False

####################################################
## 3. Control Flow
## 3. 控制流
####################################################

# Let's just make a variable
# 我们先创建一个变量
some_var = 5

# Here is an if statement. Indentation is significant in python!
# prints "some_var is smaller than 10"
# 这里有一个条件语句。缩进在 Python 中可是很重要的哦！
# 程序会打印出 "some_var is smaller than 10"
# （译注：意为“some_var 比 10 小”。）
if some_var > 10:
    print
    "some_var is totally bigger than 10."
    # （译注：意为“some_var 完全比 10 大”。）
elif some_var < 10:  # This elif clause is optional.
    # 这里的 elif 子句是可选的
    print
    "some_var is smaller than 10."
    # （译注：意为“some_var 比 10 小”。）
else:  # This is optional too.
    # 这一句也是可选的
    print
    "some_var is indeed 10."
    # （译注：意为“some_var 就是 10”。）

"""
For loops iterate over lists
for 循环可以遍历列表
prints:
如果要打印出：
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use % to interpolate formatted strings
    # 别忘了你可以使用 % 来格式化字符串
    print
    "%s is a mammal" % animal
    # （译注：意为“%s 是哺乳动物”。）

"""
`range(number)` returns a list of numbers 
from zero to the given number
`range(数字)` 会返回一个数字列表，
这个列表将包含从零到给定的数字。
prints:
如果要打印出：
    0
    1
    2
    3
"""
for i in range(4):
    print(i)


"""
While loops go until a condition is no longer met.
while 循环会一直继续，直到条件不再满足。
prints:
如果要打印出：
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print
    x
    x += 1  # Shorthand for x = x + 1
    # 这是 x = x + 1 的简写方式

# Handle exceptions with a try/except block
# 使用 try/except 代码块来处理异常

# Works on Python 2.6 and up:
# 适用于 Python 2.6 及以上版本：
try:
    # Use raise to raise an error
    # 使用 raise 来抛出一个错误
    raise IndexError("This is an index error")
    # 抛出一个索引错误：“这是一个索引错误”。
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
    # pass 只是一个空操作。通常你应该在这里做一些恢复工作。


####################################################
## 4. Functions
## 4. 函数
####################################################

# Use def to create new functions
# 使用 def 来创建新函数
def add(x, y):
    print("x is %s and y is %s" % (x, y))
    # （译注：意为“x 是 %s 而且 y 是 %s”。）
    return x + y  # Return values with a return statement
    # 使用 return 语句来返回值


# Calling functions with parameters
# 调用函数并传入参数
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11
# （译注：意为“x 是 5 而且 y 是 6”，并返回 11）

# Another way to call functions is with keyword arguments
# 调用函数的另一种方式是传入关键字参数
add(y=6, x=5)  # Keyword arguments can arrive in any order.


# 关键字参数可以以任意顺序传入

# You can define functions that take a variable number of
# positional arguments
# 你可以定义一个函数，并让它接受可变数量的定位参数。
def varargs(*args):
    return args


varargs(1, 2, 3)  # => (1,2,3)


# You can define functions that take a variable number of
# keyword arguments, as well
# 你也可以定义一个函数，并让它接受可变数量的关键字参数。
def keyword_args(**kwargs):
    return kwargs


# Let's call it to see what happens
# 我们试着调用它，看看会发生什么：
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# You can do both at once, if you like
# 你还可以同时使用这两类参数，只要你愿意：
def all_the_args(*args, **kwargs):
    print
    args
    print
    kwargs


"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of varargs/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
# 在调用函数时，定位参数和关键字参数还可以反过来用。
# 使用 * 来展开元组，使用 ** 来展开关键字参数。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)  # equivalent to foo(1, 2, 3, 4)
# 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)  # equivalent to foo(a=3, b=4)
# 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to foo(1, 2, 3, 4, a=3, b=4)


# 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# Python has first class functions
# 函数在 Python 中是一等公民
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
add_10(3)  # => 13

# There are also anonymous functions
# 还有匿名函数
(lambda x: x > 2)(3)  # => True

# There are built-in higher order functions
# 还有一些内建的高阶函数
map(add_10, [1, 2, 3])  # => [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# 我们可以使用列表推导式来模拟 map 和 filter
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]


####################################################
## 5. Classes
## 5. 类
####################################################

# We subclass from object to get a class.
# 我们可以从对象中继承，来得到一个类。
class Human(object):
    # A class attribute. It is shared by all instances of this class
    # 下面是一个类属性。它将被这个类的所有实例共享。
    species = "H. sapiens"

    # Basic initializer
    # 基本的初始化函数（构造函数）
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        # 把参数赋值为实例的 name 属性
        self.name = name

    # An instance method. All methods take self as the first argument
    # 下面是一个实例方法。所有方法都以 self 作为第一个参数。
    def say(self, msg):
        return "%s: %s" % (self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    # 类方法会被所有实例共享。
    # 类方法在调用时，会将类本身作为第一个函数传入。
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    # 静态方法在调用时，不会传入类或实例的引用。
    @staticmethod
    def grunt():
        return "*grunt*"


# Instantiate a class
# 实例化一个类
i = Human(name="Ian")
print
i.say("hi")  # prints out "Ian: hi"
# 打印出 "Ian: hi"

j = Human("Joel")
print
j.say("hello")  # prints out "Joel: hello"
# 打印出 "Joel: hello"

# Call our class method
# 调用我们的类方法
i.get_species()  # => "H. sapiens"

# Change the shared attribute
# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# Call the static method
# 调用静态方法
Human.grunt()  # => "*grunt*"

####################################################
## 6. Modules
## 6. 模块
####################################################

# You can import modules
# 你可以导入模块
import math

print
math.sqrt(16)  # => 4

# You can get specific functions from a module
# 也可以从一个模块中获取指定的函数
from math import ceil, floor

print
ceil(3.7)  # => 4.0
print
floor(3.7)  # => 3.0

# You can import all functions from a module.
# Warning: this is not recommended
# 你可以从一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *

# You can shorten module names
# 你可以缩短模块的名称
import math as m

math.sqrt(16) == m.sqrt(16)  # => True

# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.
# Python 模块就是普通的 Python 文件。
# 你可以编写你自己的模块，然后导入它们。
# 模块的名称与文件名相同。

# You can find out which functions and attributes
# defines a module.
# 你可以查出一个模块里有哪些函数和属性
import math

dir(math)