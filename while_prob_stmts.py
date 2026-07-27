#below average problems
# 1. Print natural numbers up to n
n = int(input("Enter n: "))
i = 1

print("Natural Numbers:")
while i <= n:
    print(i, end=" ")
    i += 1


# 2. Print even numbers up to n
i = 2

print("\n\nEven Numbers:")
while i <= n:
    print(i, end=" ")
    i += 2


# 3. Print odd numbers up to n
i = 1

print("\n\nOdd Numbers:")
while i <= n:
    print(i, end=" ")
    i += 2


# 4. Sum of natural numbers up to n
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("\n\nSum of Natural Numbers =", sum)

#average problems
# 1. Sum of odd numbers up to n
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 2
print("Sum of odd numbers =", sum)


# 2. Sum of even numbers up to n
n = int(input("Enter n: "))
i = 2
sum = 0
while i <= n:
    sum = sum + i
    i = i + 2
print("Sum of even numbers =", sum)


# 3. Print natural numbers up to n in reverse order
n = int(input("Enter n: "))
while n >= 1:
    print(n)
    n = n - 1


# 4. Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a = 0
b = 1
count = 1

while count <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count = count + 1


# 5. Factorial of a given number
n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1
print("\nFactorial =", fact)


#above average problems
# 1. Check whether a number is Prime or Not
n = int(input("Enter a number: "))
i = 2
flag = 0

while i <= n // 2:
    if n % i == 0:
        flag = 1
        break
    i = i + 1

if n <= 1:
    print("Not Prime")
elif flag == 0:
    print("Prime Number")
else:
    print("Not Prime")


# 2. Find the Sum of Digits
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)


# 3. Check whether a Number is Palindrome or Not
n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 4. Reverse a Number
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse Number =", rev)


#above average problems
# 1. Multiplication Table
n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1


# 2. Largest of n Numbers
n = int(input("Enter how many numbers: "))

i = 1
largest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest number =", largest)


# 3. Smallest of n Numbers
n = int(input("Enter how many numbers: "))

i = 1
smallest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest number =", smallest)
