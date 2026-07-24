Python 3.13.11 (tags/v3.13.11:6278944, Dec  5 2025, 16:26:58) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=4.45
print(type(x))
<class 'float'>
x=True
print(type(x))
<class 'bool'>
b=93
print(type(b))
<class 'int'>
type(new)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(new)
NameError: name 'new' is not defined
z=new
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    z=new
NameError: name 'new' is not defined
NameError: name 'new' is not defined
SyntaxError: invalid syntax
print(type(z))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(type(z))
NameError: name 'z' is not defined
c="hello"
print(type(c))
<class 'str'>
>>> y=[2,3,6,88,65]
>>> print(type(y))
<class 'list'>
>>> u=(4,6,7,3)
>>> print(type(u))
<class 'tuple'>
>>> h={45,6,78,98,45}
>>> print(type(h))
<class 'set'>
>>> d=[a,b,f,g]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d=[a,b,f,g]
NameError: name 'a' is not defined
>>> d=["a","b","f","g"]
>>> print(type(d))
<class 'list'>
>>> c=range(9)
>>> type(c)
<class 'range'>
>>> v=["apple","banana","cat","dog"]
>>> print(type(v))
<class 'list'>
>>> type(new)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    type(new)
NameError: name 'new' is not defined
>>> new={"name":"Apex","age":22}
>>> type(new)
<class 'dict'>
>>> c=(5,6,4,9)
>>> c.append(5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> c=[8,7,4,6]
>>> c.append(23)
>>> print(c)
[8, 7, 4, 6, 23]
>>> print(c[4])
23
>>> type(c)
<class 'list'>
