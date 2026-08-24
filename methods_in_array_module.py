from array import array

# append()
a = array('i', [10, 20, 30])
a.append(40)
print("after appending:", a)


#buffer_info()
a = array('i', [10, 20, 30])
print("buffer_info:", a.buffer_info())


# byteswap()
a = array('i', [1, 2, 3])
a.byteswap()
print("byteswap:", a)


# count()
a = array('i', [10, 20, 10, 30, 10])
print("count:", a.count(10))


# extend()
a = array('i', [10, 20])
a.extend([30, 40])
print("extend:", a)


# frombytes()
a = array('i', [10, 20])
b = array('i', [30, 40])
a.frombytes(b.tobytes())
print("frombytes:", a)


# fromfile()
a = array('i', [10, 20, 30])
with open("numbers.bin", "wb") as f:
    a.tofile(f)
b = array('i')
with open("numbers.bin", "rb") as f:
    b.fromfile(f, 3)
print("fromfile:", b)


# fromlist()
a = array('i')
a.fromlist([10, 20, 30])
print("fromlist:", a)


# fromunicode()
a = array('u')
a.fromunicode("ABC")
print("fromunicode:", a)


# index()
a = array('i', [10, 20, 30, 40])
print("index:", a.index(30))


# insert()
a = array('i', [10, 20, 40])
a.insert(2, 30)
print("insert:", a)


# pop()
a = array('i', [10, 20, 30])
a.pop()
print("pop:", a)


# remove()
a = array('i', [10, 20, 30])
a.remove(20)
print("remove:", a)


# reverse()
a = array('i', [10, 20, 30])
a.reverse()
print("reverse:", a)


# tobytes()
a = array('i', [10, 20, 30])
b = a.tobytes()
print("tobytes:", b)


# tofile()
a = array('i', [10, 20, 30])
with open("numbers2.bin", "wb") as f:
    a.tofile(f)
print("tofile: Data written to file")


# tolist()
a = array('i', [10, 20, 30])
b = a.tolist()
print("tolist:", b)


# tounicode()
a = array('u', 'ABC')
print("tounicode:", a.tounicode())