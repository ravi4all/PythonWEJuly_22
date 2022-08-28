Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sys
text = "hello world"
sys.getsizeof(str)
408
sys.getsizeof(str())
49
sys.getsizeof("")
49
sys.getsizeof("h")
50
sys.getsizeof("he")
51
sys.getsizeof(text)
60
len(text)
11
text = "hello how are you..??"
len(text)
21
text[0]
'h'
text[1]
'e'
text[8]
'w'
text[18]
'.'
text[-1]
'?'
text[-2]
'?'
text[-6]
'o'
text
'hello how are you..??'
text[0]
'h'
text[5]
' '
text[4]
'o'
text[0:4]
'hell'
text[0:14]
'hello how are '
text[0:]
'hello how are you..??'
text[:20]
'hello how are you..?'
text[10:20]
'are you..?'
text[:]
'hello how are you..??'
text[10:0]
''
text[10:0:-1]
'a woh olle'
text[5:0:-1]
' olle'
text[5::-1]
' olleh'
text[0:20]
'hello how are you..?'
text[0:20:2]
'hlohwaeyu.'
text[0:20:3]
'hlh eo.'
text[::-1]
'??..uoy era woh olleh'
text[-1:-10]
''
text[-1:-10:-1]
'??..uoy e'
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text.lower()
'hello how are you..??'
text.upper()
'HELLO HOW ARE YOU..??'
text.capitalize()
'Hello how are you..??'
text.title()
'Hello How Are You..??'
text.swapcase()
'HELLO HOW ARE YOU..??'
text
'hello how are you..??'
text.replace("hello", "bye")
'bye how are you..??'
text
'hello how are you..??'
text[0] = 'i'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    text[0] = 'i'
TypeError: 'str' object does not support item assignment
del text[0]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
text.index('y')
14
text.index('u')
16
text.index('o')
4
text.count('o')
3
text
'hello how are you..??'
text.index('o',0)
4
text.index('o',5)
7
text.index('o',8)
15
text.index('how')
6
text.index('o')
4
text.index('o',5)
7
text.index('o',8)
15
text[-1:]
'?'
text[-2:]
'??'
text[-1:-10]
''
text[-1:-10:-1]
'??..uoy e'
text[-5:]
'u..??'
text[-15:]
'how are you..??'
text.index('z')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('h')
0
text.find('i')
-1
text.find('z')
-1
text.find('o')
4
text.find('o',5)
7
count = text.count('o')
count
3
index = 0
for i in range(count):
    index = text.find('o',index)
    print("Found at :",index)
    index += 1

    
Found at : 4
Found at : 7
Found at : 15
text.rfind('o')
15
text.rindex('o')
15
text.isalnum()
False
text.isalpha()
False
text.isdigit()
False
text.islower()
True
text.isupper()
False
text.startswith('h')
True
text.startswith('t')
False
text.endswith('?')
True
text.endswith('.exe')
False
text.endswith('.jpg')
False
text.endswith('.txt')
False
msg = "open facebook"
import webbrowser
msg.split()
['open', 'facebook']
msg.split()[0]
'open'
msg.split()[1]
'facebook'
name = msg.split()[1]
if msg.startswith("open"): webbrowser.open(name+".com")

True
msg = "open twitter"
name = msg.split()[1]
if msg.startswith("open"): webbrowser.open(name+".com")

True
