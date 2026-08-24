# 1. Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

factorial(5)


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(10)


# 3. Define a function that accepts two numbers and returns the greater number.
def greater(a, b):
    if a > b:
        print(a)
    else:
        print(b)
greater(10, 20)


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print(si)
simple_interest(1000, 5, 2)


# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    flag = True
    if n < 2:
        flag = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                flag = False
                break
    print(flag)
is_prime(7)


# 6. Define a function to calculate the area of a circle using its radius.
def circle_area(r):
    area = 3.14 * r * r
    print(area)
circle_area(5)


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)
natural_sum(5)


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    print(base ** exponent)
power(2, 5)


# 9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def largest(arr):
    large = arr[0]
    for i in arr:
        if i > large:
            large = i
    print(large)
largest([10, 25, 7, 45, 18])


# 10. Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    print(count)
count_vowels("Hello World")


# 11. Write a function that accepts a string and returns its reverse.
def reverse_string(s):
    print(s[::-1])
reverse_string("Hello")


# 12. Create a function that checks whether a given string or number is a palindrome.
def palindrome(x):
    x = str(x)
    if x == x[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome("madam")


# 13. Write a function that accepts a list of numbers and returns their average.
def average(arr):
    print(sum(arr) / len(arr))
average([10, 20, 30, 40, 50])


# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_element(arr, element):
    count = 0
    for i in arr:
        if i == element:
            count += 1
    print(count)
count_element([1, 2, 2, 3, 2, 4], 2)


# 15. Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    print(result)
unique_elements([1, 2, 2, 3, 4, 4, 5])


# 16. Create a function to find the second-largest number in a list.
def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    print(unique[-2])
second_largest([10, 20, 5, 40, 30])


# 17. Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    print(result)
fibonacci(7)


# 18. Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def percentage_grade(marks):
    percentage = sum(marks) / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    print("Percentage:", percentage)
    print("Grade:", grade)
percentage_grade([85, 90, 78, 88, 92])


# 19. Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12
    print("Bill:", bill)
electricity_bill(250)


# 20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    print("Gross Salary:", gross)
gross_salary(30000)


# 21. Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def total_bill(prices, quantities, discount):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    final_bill = total - (total * discount / 100)
    print("Total Bill:", final_bill)
total_bill([100, 200, 300], [2, 1, 2], 10)


# 22. Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def statistics(arr):
    print("Minimum:", min(arr))
    print("Maximum:", max(arr))
    print("Sum:", sum(arr))
    print("Average:", sum(arr) / len(arr))
statistics([10, 20, 5, 40, 30])


# 23. Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def student_result(marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade
students = [
    ("Aniket", 1, [80, 85, 90, 75, 88]),
    ("Rahul", 2, [70, 75, 80, 72, 78]),
    ("Om", 3, [90, 92, 88, 95, 91])
]
percentages = []
for name, roll, marks in students:
    total, percentage, grade = student_result(marks)
    percentages.append(percentage)
    print(name, roll)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
print("Class Average:", sum(percentages) / len(percentages))
highest = max(students, key=lambda x: student_result(x[2])[1])
lowest = min(students, key=lambda x: student_result(x[2])[1])
print("Highest Scorer:", highest[0])
print("Lowest Scorer:", lowest[0])


# 24. Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.
balance = 0
transactions = []
def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited " + str(amount))
def withdrawal(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn " + str(amount))
    else:
        print("Insufficient Balance")
def balance_enquiry():
    print("Balance:", balance)
def transaction_history():
    print("Transactions:")
    for t in transactions:
        print(t)
deposit(5000)
withdrawal(1500)
balance_enquiry()
transaction_history()


# 25. Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
books = {}
def add_book(book_id, name):
    books[book_id] = {"name": name, "available": True}
def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book Issued")
    else:
        print("Book Not Available")
def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book Returned")
def search_book(name):
    for book in books.values():
        if book["name"].lower() == name.lower():
            print("Book Found:", book["name"])
            return
    print("Book Not Found")
def display_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["name"])
add_book(1, "Python")
add_book(2, "Java")
add_book(3, "C++")
display_books()
issue_book(1)
search_book("Java")
return_book(1)


# 26. Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.
def slab_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 500 + (units - 100) * 7
    else:
        return 1200 + (units - 200) * 10
def final_electricity_bill(units):
    fixed_charge = 100
    bill = slab_bill(units) + fixed_charge
    tax = bill * 0.05
    discount = bill * 0.02
    final = bill + tax - discount
    print("Final Bill:", final)
final_electricity_bill(250)


# 27. Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.
def consultation(charges):
    return charges
def laboratory(charges):
    return charges
def medicine(charges):
    return charges
def room(charges):
    return charges
def patient_bill(c, l, m, r, category):
    total = consultation(c) + laboratory(l) + medicine(m) + room(r)
    if category == "senior":
        total = total - total * 0.10
    elif category == "child":
        total = total - total * 0.05
    print("Final Bill:", total)
patient_bill(500, 1000, 1500, 2000, "senior")


# 28. Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
cart = {}
def add_product(name, price, quantity):
    cart[name] = [price, quantity]
def remove_product(name):
    if name in cart:
        del cart[name]
def subtotal():
    total = 0
    for price, quantity in cart.values():
        total += price * quantity
    return total
def final_invoice(coupon):
    sub = subtotal()
    if coupon == "SAVE10":
        discount = sub * 0.10
    else:
        discount = 0
    amount = sub - discount
    gst = amount * 0.18
    final = amount + gst
    print("Subtotal:", sub)
    print("Discount:", discount)
    print("GST:", gst)
    print("Final Invoice:", final)
add_product("Laptop", 50000, 1)
add_product("Mouse", 500, 2)
final_invoice("SAVE10")


# 29. Write a recursive function to search for an element in a sorted list using binary search.
def binary_search(arr, target, low, high):
    if low > high:
        print("Element not found")
        return
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Element found at index:", mid)
    elif target < arr[mid]:
        binary_search(arr, target, low, mid - 1)
    else:
        binary_search(arr, target, mid + 1, high)
arr = [10, 20, 30, 40, 50, 60]
binary_search(arr, 40, 0, len(arr) - 1)


# 30. Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end="")
decimal_to_binary(10)
print()


# 31. Check whether a string is a palindrome using recursion.
def recursive_palindrome(s, start, end):
    if start >= end:
        print("Palindrome")
        return
    if s[start] != s[end]:
        print("Not Palindrome")
        return
    recursive_palindrome(s, start + 1, end - 1)
s = "madam"
recursive_palindrome(s, 0, len(s) - 1)


# 32. Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def calculate(a, b, operation):
    print(operation(a, b))
calculate(10, 5, addition)
calculate(10, 5, subtraction)
calculate(10, 5, multiplication)
calculate(10, 5, division)


# Programs on Lambda Function
# 33. Write a lambda function to calculate the square of a given number.
square = lambda x: x ** 2
print(square(5))


# 34. Create a lambda function that returns the cube of a number.
cube = lambda x: x ** 3
print(cube(4))


# 35. Write a lambda function that returns True if a number is even and False otherwise.
even = lambda x: x % 2 == 0
print(even(10))


# 36. Use a lambda function to find the maximum of two numbers.
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))


# 37. Create a lambda function to calculate simple interest using principal, rate, and time.
simple_interest = lambda p, r, t: (p * r * t) / 100
print(simple_interest(1000, 5, 2))


# 38. Take a list of numbers, use map() and a lambda function to generate a list containing their squares.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


# 39. Use map() with lambda to calculate the cube of every element in a list.
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)


# 40. Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
result = list(map(lambda x, y: x + y, a, b))
print(result)


# 41. Take a list of integers, use filter() and lambda to extract all even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 42. Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(
    filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)),numbers))
print(prime_numbers)


# 43. Use filter() and lambda to extract positive numbers from a list.
numbers = [-5, -2, 0, 3, 7, -1, 9]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)


# 44. Take a list of numbers, use filter() and lambda to find numbers greater than 50.
numbers = [20, 45, 55, 70, 30, 90]
result = list(filter(lambda x: x > 50, numbers))
print(result)


# 45. Take a list of words, use filter() and lambda to find words having more than five characters.
words = ["apple", "banana", "cat", "orange", "computer"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)


# 46. Take a list of words; sort them according to their length using lambda.
words = ["apple", "cat", "banana", "new"]
words.sort(key=lambda x: len(x))
print(words)


# 47. Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.
students = [
    ("Adesh", 85),
    ("Sandesh",81),
    ("Rushi", 97)
]
students.sort(key=lambda x: x[1])
print(students)


# 48. Take employee records containing name and salary, sort them according to salary using lambda.
employees = [
    ("Adesh", 450000),
    ("Aryan", 60000),
    ("Parshwa", 50000)
]
employees.sort(key=lambda x: x[1])
print(employees)


# 49. Take a list containing student names and marks, use functions and lambda expressions to:
# a) Calculate average marks.
# b) Filter students scoring above 75.
# c) Sort students according to marks.
students = [
    ("Ritesh", 80),
    ("Nitesh", 85),
    ("Litesh", 90),
    ("Rushikesh", 92)
]
average_marks = sum(map(lambda x: x[1], students)) / len(students)
above_75 = list(filter(lambda x: x[1] > 75, students))
sorted_students = sorted(students, key=lambda x: x[1])
print("Average:", average_marks)
print("Above 75:", above_75)
print("Sorted:", sorted_students)


# 50. Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
# a) Find employees earning more than 50,000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.
employees = [
    ("Sanket", "IT", 45000),
    ("Shreyash", "HR", 60000),
    ("Yash", "IT", 75000),
    ("Adesh", "Sales", 50000)
]
above_50000 = list(filter(lambda x: x[2] > 50000, employees))
increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)
sorted_employees = sorted(employees, key=lambda x: x[2])
print("Above 50000:", above_50000)
print("Increased Salary:", increased_salary)
print("Sorted:", sorted_employees)


# 51. Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
# a) Calculate total value of each product.
# b) Filter products costing more than 1,000.
# c) Sort products according to total value.
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 8000, 1)
]
product_values = list(
    map(lambda x: (x[0], x[1], x[2], x[1] * x[2]), products)
)
above_1000 = list(
    filter(lambda x: x[1] > 1000, products)
)
sorted_products = sorted(
    product_values,
    key=lambda x: x[3]
)
print("Product Values:", product_values)
print("Products above 1000:", above_1000)
print("Sorted:", sorted_products)