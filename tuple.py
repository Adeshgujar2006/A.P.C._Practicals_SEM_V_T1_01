# 1. Write a Python program to create a tuple of five integers and display it.
t1 = (10, 20, 30, 40, 50)
print(t1)

# 2. Create a tuple containing five city names. Display first, last and third city.
cities = ("Mumbai", "Delhi", "Kolhapur", "Pune", "Chennai")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])

# 3. Create a tuple of student names and display the total number of students using len().
students = ("Adesh","Bhavesh","Rushi","Shivam","Yash")
print("Total students:", len(students))

# 4. Create a tuple of colors. Check whether a given color exists in the tuple.
colors = ("Red", "Green", "Blue", "Yellow")
color = input("Enter a color to search: ")
if color in colors:
    print(color, "exists in the tuple")
else:
    print(color, "does not exist in the tuple")

# 5. Create a tuple of fruits and display each fruit using a loop.
fruits = ("Apple", "Banana", "Mango", "Grapes")
for fruit in fruits:
    print(fruit)

# 6. Create a tuple with repeated numbers and count how many times a particular number appears.
nums = (1, 2, 3, 2, 4, 2, 5)
n = int(input("Enter number to count: "))
print("Count of", n, ":", nums.count(n))

# 7. Create a tuple of employee IDs and find the index of a given ID.
emp_ids = (101, 102, 103, 104, 105)
eid = int(input("Enter employee ID to find: "))
if eid in emp_ids:
    print("Index of", eid, ":", emp_ids.index(eid))
else:
    print(eid, "not found")

# 8. Create two tuples of numbers and concatenate them into a single tuple.
t_a = (1, 2, 3)
t_b = (4, 5, 6)
t_concat = t_a + t_b
print(t_concat)

# 9. Create a tuple containing three elements and repeat it four times.
t9 = (1, 2, 3)
print(t9 * 4)

# 10. Create a tuple of 10 numbers and display first five, last five, middle four, alternate, reverse.
t10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five:", t10[:5])
print("Last five:", t10[-5:])
print("Middle four:", t10[3:7])
print("Alternate elements:", t10[::2])
print("Reverse tuple:", t10[::-1])

# 11. Convert a tuple into a list and add a new element.
t11 = (1, 2, 3)
l11 = list(t11)
l11.append(4)
print(l11)

# 12. Accept five numbers from the user, store them in a list, and convert the list into a tuple.
l12 = []
for i in range(5):
    val = int(input("Enter number " + str(i + 1) + ": "))
    l12.append(val)
t12 = tuple(l12)
print(t12)

# 13. Modify a tuple by converting it into a list and then back into a tuple.
t13 = (10, 20, 30)
l13 = list(t13)
l13[1] = 99
t13 = tuple(l13)
print(t13)

# 14. Create a tuple and delete it completely.
t14 = (1, 2, 3)
print(t14)
del t14

# 15. Create a nested tuple containing student details and display each record.
students_nested = (("Adesh", 20, "CS"), ("Bhavesh", 22, "IT"), ("Parth", 20, "EC"))
for record in students_nested:
    print(record)

# 16. Store ten numbers in a tuple and calculate their sum.
t16 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Sum:", sum(t16))

# 17. Find the largest and smallest number in a tuple without using max() and min().
t17 = (23, 45, 12, 67, 34)
largest = t17[0]
smallest = t17[0]
for num in t17:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)

# 18. Calculate the average of elements stored in a tuple.
t18 = (10, 20, 30, 40, 50)
average = sum(t18) / len(t18)
print("Average:", average)

# 19. Store 15 integers in a tuple and count even and odd numbers.
t19 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even_count = 0
odd_count = 0
for num in t19:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# 20. Accept a number from the user and determine whether it exists in the tuple.
t20 = (5, 10, 15, 20, 25)
num20 = int(input("Enter a number to check: "))
if num20 in t20:
    print(num20, "exists in the tuple")
else:
    print(num20, "does not exist in the tuple")

# 21. Store student details in a tuple: Roll Number, Name, Department, Marks. Display all the details.
student21 = (1, "Amit", "Computer Science", 85)
print("Roll Number:", student21[0])
print("Name:", student21[1])
print("Department:", student21[2])
print("Marks:", student21[3])

# 22. Create tuples containing Employee ID, Name, Salary. Display all employee information.
employee22 = (201, "Rahul", 45000)
print("Employee ID:", employee22[0])
print("Name:", employee22[1])
print("Salary:", employee22[2])

# 23. Store item prices in a tuple and calculate total bill, average price, highest and lowest priced item.
prices23 = (250, 100, 450, 75, 300)
total_bill = sum(prices23)
avg_price = total_bill / len(prices23)
highest_price = max(prices23)
lowest_price = min(prices23)
print("Total bill:", total_bill)
print("Average price:", avg_price)
print("Highest-priced item:", highest_price)
print("Lowest-priced item:", lowest_price)

# 24. Store temperatures of seven days in a tuple and determine maximum, minimum, average temperature.
temps24 = (30, 32, 29, 35, 31, 28, 33)
print("Maximum temperature:", max(temps24))
print("Minimum temperature:", min(temps24))
print("Average temperature:", sum(temps24) / len(temps24))

# 25. Store runs scored in 10 matches and calculate total, highest, lowest, average score.
runs25 = (45, 67, 89, 23, 56, 78, 34, 90, 12, 65)
print("Total runs:", sum(runs25))
print("Highest score:", max(runs25))
print("Lowest score:", min(runs25))
print("Average score:", sum(runs25) / len(runs25))

# 26. Create two tuples and find the common elements between them.
t26_a = (1, 2, 3, 4, 5)
t26_b = (4, 5, 6, 7, 8)
common = tuple(set(t26_a) & set(t26_b))
print("Common elements:", common)

# 27. Merge two tuples and remove duplicate elements.
t27_a = (1, 2, 3, 4)
t27_b = (3, 4, 5, 6)
merged = tuple(set(t27_a + t27_b))
print("Merged tuple without duplicates:", merged)

# 28. Count the frequency of each element in a tuple.
t28 = (1, 2, 2, 3, 3, 3, 4)
frequency = {}
for item in t28:
    frequency[item] = t28.count(item)
print("Frequency:", frequency)

# 29. Convert a tuple into a sorted tuple in ascending and descending order.
t29 = (34, 12, 67, 23, 45)
ascending = tuple(sorted(t29))
descending = tuple(sorted(t29, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)

# 30. Create a tuple containing patient records: Patient ID, Name, Age, Blood Group.
# Display all records, search by ID, count total patients, display patients with specific blood group.
patients30 = (
    (1, "amit", 30, "A+"),
    (2, "sumit", 25, "B+"),
    (3, "Rajesh", 40, "A+"),
    (4, "Vignesh", 35, "O-"),
)

print("All records:")
for p in patients30:
    print(p)

search_id = int(input("Enter Patient ID to search: "))
found = False
for p in patients30:
    if p[0] == search_id:
        print("Patient found:", p)
        found = True
        break
if not found:
    print("Patient not found")

print("Total number of patients:", len(patients30))

blood_group = input("Enter blood group to search: ")
print("Patients with blood group", blood_group, ":")
for p in patients30:
    if p[3] == blood_group:
        print(p)