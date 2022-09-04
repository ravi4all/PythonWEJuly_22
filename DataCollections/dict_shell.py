Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = {}
type(data)
<class 'dict'>
data = {"name" : "John", "age" : 35, "salary" : 45000, "dept" : "IT"}
data
{'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT'}
data[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[0]
KeyError: 0
data[0:3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data[0:3]
TypeError: unhashable type: 'slice'
data["name"]
'John'
data["salary"]
45000
data["phone"] = 987654254
data
{'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT', 'phone': 987654254}
data.keys()
dict_keys(['name', 'age', 'salary', 'dept', 'phone'])
data.values()
dict_values(['John', 35, 45000, 'IT', 987654254])
data.items()
dict_items([('name', 'John'), ('age', 35), ('salary', 45000), ('dept', 'IT'), ('phone', 987654254)])
data.get("name")
'John'
data.get("salary")
45000
data["name"]
'John'
data["salary"]
45000
data["address"]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data["address"]
KeyError: 'address'
data.get("address")
data.get("address", "Not available")
'Not available'
data.get("name", "Not available")
'John'
data = {i : i ** 2 for i in range(1,11)}
data
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
details = {"address" : "Delhi", "phone" : 9877697655}
data
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
data = {'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT'}
data
{'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT'}
details
{'address': 'Delhi', 'phone': 9877697655}
data + details
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data + details
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
data.update(details)
data
{'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT', 'address': 'Delhi', 'phone': 9877697655}
data.pop("address")
'Delhi'
data
{'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT', 'phone': 9877697655}
data.popitem()
('phone', 9877697655)
data
{'name': 'John', 'age': 35, 'salary': 45000, 'dept': 'IT'}
for item in data:
    print(item)

    
name
age
salary
dept
for item in data:
    print(item, ":", data[item])

    
name : John
age : 35
salary : 45000
dept : IT
for item in data.values():
    print(item)

    
John
35
45000
IT

= RESTART: D:/Batches/2022/JulyPythonWE/DataCollections/dictionary_exercises.py
Shawn CS 8.9
Mac CS 6.7
Nick CS 8.6
students
{'roll_no': [4, 5, 3, 8, 12, 22, 15], 'names': ['John', 'Shawn', 'Mac', 'Sam', 'Peter', 'Sid', 'Nick'], 'branch': ['EC', 'CS', 'CS', 'EC', 'ME', 'ME', 'CS'], 'cgpa': [7.8, 8.9, 6.7, 9.0, 6.5, 4.8, 8.6]}
students["branch"]
['EC', 'CS', 'CS', 'EC', 'ME', 'ME', 'CS']
students["branch"] == "CS"
False
['EC', 'CS', 'CS', 'EC', 'ME', 'ME', 'CS'] == "CS"
False
students["branch"][0] == "CS"
False
students["branch"][1] == "CS"
True
students["roll_no"]
[4, 5, 3, 8, 12, 22, 15]
len(students["roll_no"])
7
len(students)
4
students
{'roll_no': [4, 5, 3, 8, 12, 22, 15], 'names': ['John', 'Shawn', 'Mac', 'Sam', 'Peter', 'Sid', 'Nick'], 'branch': ['EC', 'CS', 'CS', 'EC', 'ME', 'ME', 'CS'], 'cgpa': [7.8, 8.9, 6.7, 9.0, 6.5, 4.8, 8.6]}

= RESTART: D:/Batches/2022/JulyPythonWE/DataCollections/dictionary_exercises_2.py
Shawn CS 6.8
Mac CS 7.9
Nick CS 5.5
