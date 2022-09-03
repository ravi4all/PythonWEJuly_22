Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = 3,2,3,5,5
data = (3,2,3,5,5)
data = 3,2
data = 3,
type(data)
<class 'tuple'>
data = (1,3,4,5,2,5,6)
data[0]
1
data[0:3]
(1, 3, 4)
data.index(3)
1
del data[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
data[0] = 10
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data[0] = 10
TypeError: 'tuple' object does not support item assignment
data = (4)
data
4
type(data)
<class 'int'>
