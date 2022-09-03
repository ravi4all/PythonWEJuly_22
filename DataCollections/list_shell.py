Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = [3,2,5,6,2]
x = []
x = list()
x = [4,3,6,6,12.5,77.6,"python"]
x[0]
4
x[0:4]
[4, 3, 6, 6]
x[::-1]
['python', 77.6, 12.5, 6, 6, 3, 4]
dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
data = []
data.append(10)
data
[10]
data.append(20)
data
[10, 20]
data.append(15)
data
[10, 20, 15]
data.append(25,30,35,32,44,11)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data.append(25,30,35,32,44,11)
TypeError: list.append() takes exactly one argument (6 given)
data.append([25,30,35,32,44,11])
data
[10, 20, 15, [25, 30, 35, 32, 44, 11]]
data[3]
[25, 30, 35, 32, 44, 11]
del data[3]
data
[10, 20, 15]
data.extend([25,30,35,32,44,11])
data
[10, 20, 15, 25, 30, 35, 32, 44, 11]
data.insert(3,29)
data
[10, 20, 15, 29, 25, 30, 35, 32, 44, 11]
data[0]
10
data[0] = 11
dara
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dara
NameError: name 'dara' is not defined. Did you mean: 'data'?
data
[11, 20, 15, 29, 25, 30, 35, 32, 44, 11]
data.pop()
11
data
[11, 20, 15, 29, 25, 30, 35, 32, 44]
data.pop()
44
data
[11, 20, 15, 29, 25, 30, 35, 32]
data.pop(4)
25
data
[11, 20, 15, 29, 30, 35, 32]
x = data.pop(5)
x
35
data
[11, 20, 15, 29, 30, 32]
data.remove(3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data.remove(3)
ValueError: list.remove(x): x not in list
data.remove(30)
data
[11, 20, 15, 29, 32]
data.count(20)
1
data.reverse()
data
[32, 29, 15, 20, 11]
data.sort()
data
[11, 15, 20, 29, 32]
data.sort(reverse=True)
data
[32, 29, 20, 15, 11]
data = [3,1,4,7,8,5,4,8,9]
sorted(data)
[1, 3, 4, 4, 5, 7, 8, 8, 9]
sorted(data, reverse=True)
[9, 8, 8, 7, 5, 4, 4, 3, 1]
data
[3, 1, 4, 7, 8, 5, 4, 8, 9]
data.sort()
data
[1, 3, 4, 4, 5, 7, 8, 8, 9]
len(data)
9
for i in range(len(data)):
    print(i,",",data[i])

    
0 , 1
1 , 3
2 , 4
3 , 4
4 , 5
5 , 7
6 , 8
7 , 8
8 , 9
for i in range(len(data)):
    print(i,":",data[i])

    
0 : 1
1 : 3
2 : 4
3 : 4
4 : 5
5 : 7
6 : 8
7 : 8
8 : 9
for item in data:
    print(item)

    
1
3
4
4
5
7
8
8
9
data = []
for i in range(25):
    if i % 2 == 0:
        data.append(i)

        
data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
data = [i for i in range(25)]
data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
data = [i for i in range(25) if i % 2 == 0]
data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
data = [3,1,4,7,9,4,5,7,12,3,16]
data_2 = [i for i in data if i > 6]
data_2
[7, 9, 7, 12, 16]
names = ["John","Max","Sam","Sid","Tom","Nick","Smith"]
names_2 = [name for name in names if name.startswith("S")]
names_2
['Sam', 'Sid', 'Smith']
names_2 = []
for name in names:
    print(name)

    
John
Max
Sam
Sid
Tom
Nick
Smith
for name in names:
    if name.startswith("S"):
        names_2.append(name)

        
names_2
['Sam', 'Sid', 'Smith']
names_2 = [name for name in names if name.startswith("S")]
cubes = [i ** 3 for i in rangw(10)]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    cubes = [i ** 3 for i in rangw(10)]
NameError: name 'rangw' is not defined. Did you mean: 'range'?
cubes = [i ** 3 for i in range(10)]
cubes
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
names
['John', 'Max', 'Sam', 'Sid', 'Tom', 'Nick', 'Smith']
salary = [45000,48000,35000,70000,65000,50000,45000]
dept = ["IT", "IT", "HR", "HR", "Sales", "Admin", "Sales"]
dept
['IT', 'IT', 'HR', 'HR', 'Sales', 'Admin', 'Sales']
names
['John', 'Max', 'Sam', 'Sid', 'Tom', 'Nick', 'Smith']
salary
[45000, 48000, 35000, 70000, 65000, 50000, 45000]
dept
['IT', 'IT', 'HR', 'HR', 'Sales', 'Admin', 'Sales']
employees = [names, salary, dept]
employees
[['John', 'Max', 'Sam', 'Sid', 'Tom', 'Nick', 'Smith'], [45000, 48000, 35000, 70000, 65000, 50000, 45000], ['IT', 'IT', 'HR', 'HR', 'Sales', 'Admin', 'Sales']]
employees[0]
['John', 'Max', 'Sam', 'Sid', 'Tom', 'Nick', 'Smith']
employees[1]
[45000, 48000, 35000, 70000, 65000, 50000, 45000]
employees[2]
['IT', 'IT', 'HR', 'HR', 'Sales', 'Admin', 'Sales']
employees[0][0]
'John'
employees[1][0]
45000
employees[2][0]
'IT'
for i in range(len(names)):
    print(employees[0][i], employees[1][i], employees[2][i])

    
John 45000 IT
Max 48000 IT
Sam 35000 HR
Sid 70000 HR
Tom 65000 Sales
Nick 50000 Admin
Smith 45000 Sales
