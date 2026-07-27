#For_loop_programs

#1.
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     print(i)

#2.
# n = int(input("Enter n: "))

# for i in range(2, n + 1, 2):
#     print(i)


#3.
# n = int(input("Enter n: "))

# for i in range(1, n + 1, 2):
#     print(i)

# 4.
# n = int(input("Enter number of terms: "))

# a = 1

# for i in range(n):
#     print(a, end=" ")
#     a = a * 2

#5.
# n = int(input("Enter n: "))

# fact = 1
# sum = 1

# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + (1 / fact)

# print("Sum =", sum)

#6.
# x = float(input("Enter x: "))
# n = int(input("Enter number of terms: "))

# sum = 1

# for i in range(1, n):
#     fact = 1
#     power = 2 * i

#     for j in range(1, power + 1):
#         fact = fact * j

#     term = (x ** power) / fact

#     if i % 2 == 1:
#         sum = sum - term
#     else:
#         sum = sum + term

# print("cos(x) =", sum)

#7.
# import math

# num = int(input("Enter number: "))

# root = int(math.sqrt(num))

# count = 0

# for i in range(1, root + 1):
#     if root % i == 0:
#         count += 1

# if count == 2:
#     print(root, "is Prime")
# else:
#     print(root, "is Not Prime")

#8.
# for i in range(3):
#     for j in range(65, 68):
#      print(chr(j), end=" ")

#9.
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(65, 65 + i):
#         print(chr(j), end=" ")
#     print()

#10.
# n = int(input("Enter n: "))

# for i in range(n, 0, -1):
#     for j in range(65, 65 + i):
#         print(chr(j), end=" ")
#     print()

#11.
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

#12.
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()