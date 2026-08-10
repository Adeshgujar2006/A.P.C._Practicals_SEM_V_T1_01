# # Q1. Write a Python program to create a list of five fruits and display the list.
# fruits = []
# for i in range(5):
#     fruit = input(f"Enter fruit {i + 1}: ")
#     fruits.append(fruit)
# print("List of fruits:", fruits)


# # Q2. Create a list of five integers. Display first, last, and third element.
# numbers = []
# for i in range(5):
#     n = int(input(f"Enter integer {i + 1}: "))
#     numbers.append(n)
# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# print("Third element:", numbers[2])


# # Q3. Create a list of colors. Replace the third color with another color and display.
# colors = []
# for i in range(5):
#     c = input(f"Enter color {i + 1}: ")
#     colors.append(c)
# new_color = input("Enter new color to replace the third color: ")
# colors[2] = new_color
# print("Updated list of colors:", colors)


# # Q4. Create a list of numbers. Add one element at end, beginning, and a specified position.
# def list_of_nums():
#     count = int(input("Enter the no. of integers u want to enter: "))
#     nums = []
#     for i in range(count):
#         n = int(input(f"Enter the integer no.{i+1}: "))
#         nums.append(n)
#     print("list of numbers initially:", nums)

#     new_num = int(input("Enter the number u want to enter at end of list: "))
#     nums.append(new_num)
#     print("Updated list of integers:", nums)

#     num_at_begin = int(input("Enter the element u want to enter at beginning: "))
#     nums.insert(0, num_at_begin)
#     print("Updated list after inserting at beginning:", nums)

#     s = int(input("Enter the specified index no. u want to enter: "))

#     new_no = int(input("Enter the element u want to enter at specified position: "))
#     nums.insert(s, new_no)
#     print("Final updated list:", nums)

# list_of_nums()


#  Q5. Create a list of student names. Remove first, last, and a specific student.
# def names_of_students():
#     l = input("Enter the names of students (separated by spaces): ").split()
#     print("Initial list:", l)

#     l.pop(0)
#     print("List after removing first element:", l)

#     l.pop()
#     print("List after removing last element:", l)

#     specific_student = input("Enter the name of specified student u want to remove: ")
#     if specific_student in l:
#         l.remove(specific_student)
#         print("Updated Final list:", l)
#     else:
#         print(f"'{specific_student}' not found in the list.")

# names_of_students()



#  Q6. Find the largest and smallest number in a list without using max() or min().
# values = []
# count = int(input("How many numbers do you want to enter? "))
# for i in range(count):
#     v = int(input(f"Enter number {i + 1}: "))
#     values.append(v)
# largest = values[0]
# smallest = values[0]
# for v in values:
#     if v > largest:
#         largest = v
#     if v < smallest:
#         smallest = v
# print("Largest number:", largest)
# print("Smallest number:", smallest)


# Q7. Accept 10 numbers from the user, store in a list. Calculate sum and average.
# num_list = []
# for i in range(10):
#     n = int(input(f"Enter number {i + 1}: "))
#     num_list.append(n)
# total = sum(num_list)
# average = total / len(num_list)
# print("Sum:", total)
# print("Average:", average)


# Q8. Store 15 integers in a list. Count how many numbers are even and odd.
# int_list = []
# for i in range(15):
#     n = int(input(f"Enter integer {i + 1}: "))
#     int_list.append(n)
# even_count = 0
# odd_count = 0
# for n in int_list:
#     if n % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers count:", even_count)
# print("Odd numbers count:", odd_count)


#  Q9. Create a list of cities. Ask user to enter a city name and check if it exists.
# cities = []
# count = int(input("How many cities do you want to enter? "))
# for i in range(count):
#     c = input(f"Enter city {i + 1}: ")
#     cities.append(c)
# city_input = input("Enter a city name to search: ")
# if city_input in cities:
#     print(city_input, "exists in the list.")
# else:
#     print(city_input, "does not exist in the list.")


#  Q10. Write a program to reverse a list without using the reverse() method.
# original = []
# count = int(input("How many numbers do you want to enter? "))
# for i in range(count):
#     n = int(input(f"Enter number {i + 1}: "))
#     original.append(n)
# reversed_list = []
# for i in range(len(original) - 1, -1, -1):
#     reversed_list.append(original[i])
# print("Reversed list:", reversed_list)


# Q11. Create a list of 10 numbers and display first 5, last 5, middle 4,

# lst = []
# for i in range(10):
#     n = int(input(f"Enter number {i + 1}: "))
#     lst.append(n)
# print("First 5 elements:", lst[:5])
# print("Last 5 elements:", lst[-5:])
# print("Middle 4 elements:", lst[3:7])
# print("Alternate elements:", lst[::2])
# print("Reversed list:", lst[::-1])


#  Q12. Display all elements present at even index positions.
# data = []
# count = int(input("How many numbers do you want to enter? "))
# for i in range(count):
#     n = int(input(f"Enter number {i + 1}: "))
#     data.append(n)
# even_index_elements = data[::2]
# print("Elements at even index positions:", even_index_elements)


# Q13. Accept 10 numbers and sort them in ascending and descending order.
# input_numbers = []
# for i in range(10):
#     n = int(input(f"Enter number {i + 1}: "))
#     input_numbers.append(n)
# ascending = sorted(input_numbers)
# descending = sorted(input_numbers, reverse=True)
# print("Ascending order:", ascending)
# print("Descending order:", descending)


#  Q14. Create a list containing duplicate values and display only unique elements.
# dup_list = []
# count = int(input("How many numbers do you want to enter (duplicates allowed)? "))
# for i in range(count):
#     n = int(input(f"Enter number {i + 1}: "))
#     dup_list.append(n)
# unique_elements = list(set(dup_list))
# print("Unique elements:", unique_elements)


#  Q15. Find the second largest element in a list.
# nums2 = []
# count = int(input("How many numbers do you want to enter? "))
# for i in range(count):
#     n = int(input(f"Enter number {i + 1}: "))
#     nums2.append(n)
# sorted_nums = sorted(nums2, reverse=True)
# second_largest = sorted_nums[1]
# print("Second largest element:", second_largest)


# Q16. Create a nested list storing Student Name, Roll Number, and Marks.

# student_records = []
# count = int(input("How many students do you want to enter? "))
# for i in range(count):
#     name = input(f"Enter name of student {i + 1}: ")
#     roll = int(input(f"Enter roll number of student {i + 1}: "))
#     marks = int(input(f"Enter marks of student {i + 1}: "))
#     student_records.append([name, roll, marks])
# for record in student_records:
#     print(f"Name: {record[0]}, Roll No: {record[1]}, Marks: {record[2]}")


#  Q17. Create two 3x3 matrices using nested lists and perform matrix addition.
# print("Enter elements for Matrix A (3x3):")
# matrix_a = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         val = int(input(f"Matrix A [{i}][{j}]: "))
#         row.append(val)
#     matrix_a.append(row)

# print("Enter elements for Matrix B (3x3):")
# matrix_b = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         val = int(input(f"Matrix B [{i}][{j}]: "))
#         row.append(val)
#     matrix_b.append(row)

# result_matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(matrix_a[i][j] + matrix_b[i][j])
#     result_matrix.append(row)
# print("Resultant Matrix after addition:")
# for row in result_matrix:
#     print(row)


#Q18. Create a shopping cart using a list.

# cart = []
# count = int(input("How many items do you want to enter in the cart? "))
# for i in range(count):
#     item = input(f"Enter item {i + 1}: ")
#     cart.append(item)
# add_item = input("Enter an item to add to the cart: ")
# cart.append(add_item)
# remove_item = input("Enter an item to remove from the cart: ")
# if remove_item in cart:
#     cart.remove(remove_item)
# search_item = input("Enter an item to search in the cart: ")
# found = search_item in cart
# print("Cart after operations:", cart)
# print(f"Is '{search_item}' in cart?:", found)
# print("Total items in cart:", len(cart))


# Q19. Store names of students present in class.

# present_students = []
# count = int(input("How many students are present in class? "))
# for i in range(count):
#     name = input(f"Enter name of present student {i + 1}: ")
#     present_students.append(name)
# print("Total students present:", len(present_students))
# search_name = input("Enter a student's name to check attendance: ")
# print(f"Is '{search_name}' present?:", search_name in present_students)
# new_student = input("Enter the name of a new student to add: ")
# present_students.append(new_student)
# absent_student = input("Enter the name of an absent student to remove: ")
# if absent_student in present_students:
#     present_students.remove(absent_student)
# print("Updated attendance list:", present_students)


# Q20. Create a list of books.

# books = []
# count = int(input("How many books do you want to enter? "))
# for i in range(count):
#     book = input(f"Enter book {i + 1}: ")
#     books.append(book)
# new_book = input("Enter a new book to add: ")
# books.append(new_book)
# search_book = input("Enter a book name to search: ")
# print(f"Is '{search_book}' available?:", search_book in books)
# remove_book = input("Enter a book name to remove: ")
# if remove_book in books:
#     books.remove(remove_book)
# print("All books:", books)
# print("Total number of books:", len(books))


#  Q21. Accept two lists and merge them into a single list.
# list1 = []
# count1 = int(input("How many elements in the first list? "))
# for i in range(count1):
#     n = input(f"Enter element {i + 1} for list 1: ")
#     list1.append(n)

# list2 = []
# count2 = int(input("How many elements in the second list? "))
# for i in range(count2):
#     n = input(f"Enter element {i + 1} for list 2: ")
#     list2.append(n)

# merged_list = list1 + list2
# print("Merged list:", merged_list)


# Q22. Find common elements between two lists.
# listA = []
# countA = int(input("How many elements in list A? "))
# for i in range(countA):
#     n = input(f"Enter element {i + 1} for list A: ")
#     listA.append(n)

# listB = []
# countB = int(input("How many elements in list B? "))
# for i in range(countB):
#     n = input(f"Enter element {i + 1} for list B: ")
#     listB.append(n)

# common_elements = [x for x in listA if x in listB]
# print("Common elements:", common_elements)


# Q23. Count the frequency of each element in a list.
# freq_list = []
# count = int(input("How many elements do you want to enter? "))
# for i in range(count):
#     item = input(f"Enter element {i + 1}: ")
#     freq_list.append(item)
# frequency = {}
# for item in freq_list:
#     frequency[item] = frequency.get(item, 0) + 1
# print("Frequency of each element:", frequency)


# Q24. Rotate a list left by one position and right by one position.
# rotate_list = []
# count = int(input("How many elements do you want to enter? "))
# for i in range(count):
#     n = input(f"Enter element {i + 1}: ")
#     rotate_list.append(n)
# left_rotated = rotate_list[1:] + rotate_list[:1]
# right_rotated = rotate_list[-1:] + rotate_list[:-1]
# print("Left rotated list:", left_rotated)
# print("Right rotated list:", right_rotated)


#Q25. Remove all duplicate elements while preserving the original order.
# dup_order_list = []
# count = int(input("How many elements do you want to enter (duplicates allowed)? "))
# for i in range(count):
#     item = input(f"Enter element {i + 1}: ")
#     dup_order_list.append(item)
# seen = set()
# result_no_dup = []
# for item in dup_order_list:
#     if item not in seen:
#         result_no_dup.append(item)
#         seen.add(item)
# print("List without duplicates (order preserved):", result_no_dup)


# Q26. Store marks of 20 students in a list and determine highest, lowest,

# marks = []
# for i in range(20):
#     m = int(input(f"Enter marks of student {i + 1}: "))
#     marks.append(m)
# highest_marks = max(marks)
# lowest_marks = min(marks)
# average_marks = sum(marks) / len(marks)
# above_avg = len([m for m in marks if m > average_marks])
# below_avg = len([m for m in marks if m < average_marks])
# print("Highest marks:", highest_marks)
# print("Lowest marks:", lowest_marks)
# print("Average marks:", average_marks)
# print("Students scoring above average:", above_avg)
# print("Students scoring below average:", below_avg)


# Q27. Store salaries of employees and determine highest, lowest, average salary,

# salaries = []
# count = int(input("How many employees do you want to enter? "))
# for i in range(count):
#     s = float(input(f"Enter salary of employee {i + 1}: "))
#     salaries.append(s)
# highest_salary = max(salaries)
# lowest_salary = min(salaries)
# average_salary = sum(salaries) / len(salaries)
# above_50000 = len([s for s in salaries if s > 50000])
# below_30000 = len([s for s in salaries if s < 30000])
# print("Highest salary:", highest_salary)
# print("Lowest salary:", lowest_salary)
# print("Average salary:", average_salary)
# print("Employees earning above 50,000:", above_50000)
# print("Employees earning below 30,000:", below_30000)


 # Q28. Store scores of a batsman in 10 matches and calculate highest, lowest,

# scores = []
# for i in range(10):
#     s = int(input(f"Enter score in match {i + 1}: "))
#     scores.append(s)
# highest_score = max(scores)
# lowest_score = min(scores)
# total_runs = sum(scores)
# average_runs = total_runs / len(scores)
# centuries = len([s for s in scores if s >= 100])
# half_centuries = len([s for s in scores if 50 <= s < 100])
# print("Highest score:", highest_score)
# print("Lowest score:", lowest_score)
# print("Total runs:", total_runs)
# print("Average runs:", average_runs)
# print("Number of centuries:", centuries)
# print("Number of half-centuries:", half_centuries)


# Q29. Store the temperature of 30 days and determine hottest, coldest day,

# temperatures = []
# for i in range(30):
#     t = float(input(f"Enter temperature of day {i + 1}: "))
#     temperatures.append(t)
# hottest_day = max(temperatures)
# coldest_day = min(temperatures)
# average_temp = sum(temperatures) / len(temperatures)
# above_avg_days = len([t for t in temperatures if t > average_temp])
# below_avg_days = len([t for t in temperatures if t < average_temp])
# print("Hottest day temperature:", hottest_day)
# print("Coldest day temperature:", coldest_day)
# print("Average temperature:", average_temp)
# print("Days above average temperature:", above_avg_days)
# print("Days below average temperature:", below_avg_days)


# # Q30. Store patient names and ages using lists.

# patient_names = []
# patient_ages = []
# count = int(input("How many patients do you want to enter? "))
# for i in range(count):
#     name = input(f"Enter name of patient {i + 1}: ")
#     age = int(input(f"Enter age of patient {i + 1}: "))
#     patient_names.append(name)
#     patient_ages.append(age)


# new_patient_name = input("Enter the name of a new patient to add: ")
# new_patient_age = int(input("Enter the age of the new patient: "))
# patient_names.append(new_patient_name)
# patient_ages.append(new_patient_age)


# delete_patient = input("Enter the name of a patient to delete: ")
# if delete_patient in patient_names:
#     del_index = patient_names.index(delete_patient)
#     patient_names.pop(del_index)
#     patient_ages.pop(del_index)


# search_patient = input("Enter the name of a patient to search: ")
# if search_patient in patient_names:
#     idx = patient_names.index(search_patient)
#     print(f"Patient found: {search_patient}, Age: {patient_ages[idx]}")
# else:
#     print(f"Patient '{search_patient}' not found.")


# print("All patients:")
# for name, age in zip(patient_names, patient_ages):
#     print(f"Name: {name}, Age: {age}")


# print("Total number of patients:", len(patient_names))