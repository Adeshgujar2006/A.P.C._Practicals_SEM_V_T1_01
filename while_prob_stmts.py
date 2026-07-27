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
