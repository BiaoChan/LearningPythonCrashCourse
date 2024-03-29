# LearningPythonCrashCourse

This is backup of my exercises from the book "Python Crash Course".

As a record of learning python.

References of updates and errors: https://ehmatthes.github.io/pcc/updates.html

## 第一章 起步  
  
#### 搭建python编程环境  
[下载安装包并安装](https://www.python.org/downloads/)  
注意安装时选中Add to path  
  
#### 安装文本编辑器  
[下载地址](geany.org)  
  
  
## 第二章 变量和简单数据类型  
  
#### 字符串  
  
开头大写 str.title()  
全部大写 str.upper()  
全部小写 str.lower()  
合并字符串 +  
删除空白 str.rstrip() str.lstrip() str.strip() 可针对空格，换行，制表符  
原始字符串： r"..." or  r'...'  
将字符串中的单词a替换成单词b: 货的返回值string.replace(a,b)， 原string不变  
string.split() 根据字符串创建一个单词列表  
string.count(word) 返回一个数值， 表示word在字符串string中出现的次数  
#### 数字  
  
可对整数执行加减乘除运算，3/2 = 1.5  
乘方：**  
str(num),将num转换成字符串  
  
#### 注释  
  
#井号后为注释内容  
  
#### python之禅  
import this  
  
## 第三章 列表简介  
  
python中用[]来表示列表，并用逗号分隔其中的元素  
访问列表元素索引从0开始，指定-1返回最后一个列表元素，-2-3以此类推  
  
#### 修改、添加、删除元素  
修改元素：直接赋值修改  
在末尾添加元素：list.append(elem)  
在列表中插入元素：list.insert（index，elem）  
删除元素：del list[index]  
弹出最后一个元素并返回弹出值：list.pop()  
弹出任意位置的元素：list.pop(index)  
删除列表中第一个指定元素：list.remove(elem)  
  
  
#### 组织列表  
字母顺序排序 list.sort()  
反序字幕排序 list.sort(reverse=True)  
临时排序,返回临时排序的列表 sorted(list) sorted(list,reverse=True)  
反转列表 list.reverse()  
列表长度 len(list)  
  
## 第四章 操作列表  
  
#### 遍历  
格式 for item in list_of_items:  
修改列表中的元素： for index in range(len(list)):  
#### 创建数值列表  
range(start,end,step) 产生一系列的数字  
  
用法：  
for value in range(1,11,2):  
  
创建数字列表 list() 可将range()的结果直接转换为列表  
numbers = list(range(1,6))  
  
简单统计功能：  
min(digit_list)  
max(digit_list)  
sum(digit_list)  
列表解析：squares = [value**2 for value in range(1,11)]  
  
#### 使用列表的一部分  
切片 ：  
list[strat:end]  
list[start:]  
list[:end]  
list[-3:] 截取列表末尾的三位  
  
遍历切片：  
for elem in list[start:end]:  
  
复制列表：  
list2 = list[start:end]  
如直接赋值则指向同一个列表  
  
  
#### 元组  
不可变的列表称为元组  
tuple = (elem1,elem2,...)  
元组的元素值不可以修改但是可以给元组变量赋值  
  
  
## 第五章 if语句  
  
#### 条件判断  
检查是否相等：==  
检查是否不相等：!=  
使用and、or可将两个条件测试合而为一  
判断特定值是否包含在列表中：elem in list  
判断特定值不包含于列表中：elem not in list  
  
## 第六章 字典  
  
dictionary = {key:value, key2:value2'...}  
修改或添加键值对：dictionary[key] = value  
删除键值对： del dictionary[key]  
  
#### 遍历字典  
遍历字典中的所有键值对：for key, value in dictionary.items():  
遍历字典中的所有键：for key in dictionary:   或 for key in dictionary.keys():  
遍历字典中的所有值: for value in dictionary.values():  
  
set() 创建一个不重复的列表  
  
#### 嵌套  
将一系列字典存储在列表中，或将列表作为值存储在字典中等。  
  
  
## 第七章 用户输入和while循环  
  
#### 用户输入  
用户输入：message = input(prompt)  
int() 将数字字符串转换为数值  
求模运算符（%）：将两个数相除并返回余数  
  
#### while循环  
用法：while condition：  
break 可以推出while循环，也可退出遍历列表或字典的for循环  
continue 返回到循环开头，并根据条件测试结果决定是否继续执行循环  
while循环可用于处理修改列表和字典，for循环则不适用于修改列表  
  
  
## 第八章 函数  
  
#### 定义函数  
def function(parameter):  
禁止修改函数列表：直接传递   列表副本 function_name(list_name[:])  
传递任意数量的实参：def function(parameter1, \*paramater2)  
传递任意数量的关键词实参：  
def function(\*\*dictionary)  
function(key=value)  
  
#### 将函数存储再模块中  
导入模块：  
import module  
使用模块中的函数：  
module.function()  
导入特定的函数,可以直接使用：  
from module import function  
from module import function1, function2, function3  
  
给函数指定别名：form module import function as f 此时function不再可用  
给模块指定别名：import module as m 此时m不再可用  
  
导入模块中的所有函数：from module import *  
  
## 第九章 类  
init前后的下划线为双下划线: \_\_init__  
继承类初始化：super().\_\_init__(...)  
导入类： form module import Class  
导入多个类：from module import Class1, Class2  
导入整个模块：import module  
导入所有类：from module import *  
  
#### python标准库  
导入模块collections中的OrderedDict类：from collections import OrderedDict  
  
随机数类：from random import randint  
  
标准库资源网：http://pymotw.com/  
  
  
## 第十章 文件和异常  
  
#### 从文件中读取数据  
打开文件 with open(filename) as file_object:  
读取文件的全部内容：contants = file_object.read() 内容以空行结尾  
逐行读取： for line in file_object:  
创建一个包含文件内各行内容的列表：lines = file_object.readlines()  
  
#### 写入文件  
'w' 写入模式，如存在文件则清空  
'r' 读取模式  
'a' 附加模式  
'r+' 读取和写入  
  
写入空文件：with open(filename, 'w') as file_object:  
write函数：file_object.write(string), 不会在末尾加入换行符  
  
附加到文件：with open(filename, 'a') as file_object:  
  
#### 异常  
格式：  
try:  
except Error:  
else:  
  
pass语句：什么都不做  
  
#### 存储数据  
导入json模块：import json  
写入json文件：json.dump(data, file_object)  
读取json文件：data = json.load(file_object)  
  
## 第十一章 测试代码  
#### 断言函数  
assertEqual(a, b)  
assertNotEqual(a, b)  
assertTrue(x)  
assertFalse(x)  
assertIn(item, list)  
assertNotIn(item, list)  
  
#### 测试函数  
导入测试模块 import unittest  
创建测试实例类 class FunctionTestCase(unittest.TestCase):  
运行测试: unittest.main()  
  
  
#### 测试类  
setUp() 自动运行，可在setUp()方法中创建一系列实例并设置他们的属性，再在测试方法中直接使用这些实例  
