# LearningPythonCrashCourse

This is backup of my exercises from the book "Python Crash Course".

As a record of learning python.

References of updates and errors: https://ehmatthes.github.io/pcc/updates.html

## 第一章 起步  

### 搭建python编程环境  
[下载安装包并安装](https://www.python.org/downloads/)  
注意安装时选中Add to path  

### 安装文本编辑器  
 [下载地址](geany.org)  


## 第二章 变量和简单数据类型  

### 字符串  

开头大写 str.title()  
全部大写 str.upper()  
全部小写 str.lower()  
合并字符串 +  
删除空白 str.rstrip() str.lstrip() str.strip() 可针对空格，换行，制表符  

### 数字  

可对整数执行加减乘除运算，3/2 = 1.5  
乘方：**  
str(num),将num转换成字符串  

### 注释  

#井号后为注释内容  

### python之禅  
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
