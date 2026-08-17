# # 1. Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
# student = {"roll_no": 1, "name": "Adesh", "department": "CS", "marks": 85}
# for key, value in student.items():
#     print(key, ":", value)

# # 2. Create a dictionary containing employee information and display the value associated with a specified key.
# employee2 = {"id": 101, "name": "abc", "salary": 45000, "department": "IT"}
# key2 = input("Enter key to search: ")
# if key2 in employee2:
#     print(employee2[key2])
# else:
#     print("Key not found")

# # 3. Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
# products3 = {"Pen": 10, "Book": 50, "Bag": 500, "Bottle": 150, "Pencil": 5}
# new_product = input("Enter new product name: ")
# new_price = float(input("Enter price: "))
# products3[new_product] = new_price
# print(products3)

# # 4. Create a dictionary containing student marks. Update the marks of a specified student.
# marks4 = {"xyz": 85, "lmn": 90, "pqr": 78}
# name4 = input("Enter student name to update: ")
# new_marks = int(input("Enter new marks: "))
# if name4 in marks4:
#     marks4[name4] = new_marks
#     print(marks4)
# else:
#     print("Student not found")

# # 5. Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
# cities5 = {"Mumbai": 20000000, "Kolhapur":850000,"Amravti":900000,"Nagpur":3000000}
# city5 = input("Enter city to remove: ")
# if city5 in cities5:
#     del cities5[city5]
#     print(cities5)
# else:
#     print("City not found")

# # 6. Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
# emp_dict6 = {101: "lmn", 102: "abc", 103: "xyz"}
# eid6 = int(input("Enter employee ID to check: "))
# if eid6 in emp_dict6:
#     print("Employee exists:", emp_dict6[eid6])
# else:
#     print("Employee ID does not exist")

# # 7. Create a dictionary containing student records and find the total number of key-value pairs.
# records7 = {"roll_no": 5, "name": "Yash", "department": "CS", "marks": 85}
# print("Total key-value pairs:", len(records7))

# # 8. Create a dictionary and display all keys, all values, all key-value pairs.
# dict8 = {"a": 1, "b": 2, "c": 3}
# print("Keys:", list(dict8.keys()))
# print("Values:", list(dict8.values()))
# print("Key-value pairs:", list(dict8.items()))

# # 9. Create a dictionary of programming languages and their creators. Display each key and value using a loop.
# languages9 = {"Python": "Guido van Rossum", "Java": "James Gosling", "C++": "Bjarne Stroustrup"}
# for language, creator in languages9.items():
#     print(language, "-", creator)

# # 10. Accept five student names and their marks from the user and store them in a dictionary.
# students10 = {}
# for i in range(5):
#     name10 = input("Enter student name: ")
#     marks10 = int(input("Enter marks: "))
#     students10[name10] = marks10
# print(students10)

# # 11. Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
# marks11 = {"Amit": 85, "Riya": 90, "Sara": 78}
# highest_student = max(marks11, key=marks11.get)
# print("Highest scorer:", highest_student, "with marks", marks11[highest_student])

# # 12. Create a dictionary containing student names and marks. Find the student with the lowest marks.
# marks12 = {"Amit": 85, "Riya": 90, "Sara": 78}
# lowest_student = min(marks12, key=marks12.get)
# print("Lowest scorer:", lowest_student, "with marks", marks12[lowest_student])

# # 13. Create a dictionary containing student names and marks. Calculate the average marks of all students.
# marks13 = {"ghanshyam": 85, "ram": 90, "Shyam": 78}
# average13 = sum(marks13.values()) / len(marks13)
# print("Average marks:", average13)

# # 14. Accept a string from the user and create a dictionary containing each character and its frequency.
# string14 = input("Enter a string: ")
# char_freq14 = {}
# for char in string14:
#     char_freq14[char] = char_freq14.get(char, 0) + 1
# print(char_freq14)

# # 15. Accept a sentence and create a dictionary containing each word and the number of times it occurs.
# sentence15 = input("Enter a sentence: ")
# words15 = sentence15.split()
# word_freq15 = {}
# for word in words15:
#     word_freq15[word] = word_freq15.get(word, 0) + 1
# print(word_freq15)

# # 16. Create two dictionaries and merge them into a single dictionary.
# dict16_a = {"a": 1, "b": 2}
# dict16_b = {"c": 3, "d": 4}
# merged16 = {**dict16_a, **dict16_b}
# print(merged16)

# # 17. Given two dictionaries, find the keys that are common to both dictionaries.
# dict17_a = {"a": 1, "b": 2, "c": 3}
# dict17_b = {"b": 4, "c": 5, "d": 6}
# common_keys = dict17_a.keys() & dict17_b.keys()
# print("Common keys:", common_keys)

# # 18. Given two dictionaries, identify the values that are common to both dictionaries.
# dict18_a = {"a": 1, "b": 2, "c": 3}
# dict18_b = {"x": 2, "y": 3, "z": 4}
# common_values = set(dict18_a.values()) & set(dict18_b.values())
# print("Common values:", common_values)

# # 19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
# dict19 = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
# seen_values = set()
# unique_dict19 = {}
# for key, value in dict19.items():
#     if value not in seen_values:
#         unique_dict19[key] = value
#         seen_values.add(value)
# print(unique_dict19)

# # 20. Create a dictionary and display its elements in ascending order of keys.
# dict20 = {"c": 3, "a": 1, "b": 2}
# for key in sorted(dict20):
#     print(key, ":", dict20[key])

# # 21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
# squares21 = {}
# for i in range(1, 11):
#     squares21[i] = i ** 2
# print(squares21)

# # 22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
# squares = {}
# for i in range(1, 21):
#     if i % 2 == 0:
#         squares22[i] = i ** 2
# print(squares22)

# # 23. Given a list of numbers, create a dictionary containing each unique number and its frequency.
# numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# freq = {}
# for num in numbers23:
#     freq23[num] = freq23.get(num, 0) + 1
# print(freq23)

# # 24. Create a dictionary containing integers from 1 to 10 and their cubes.
# cubes= {}
# for i in range(1, 11):
#     cubes24[i] = i ** 3
# print(cubes24)

# # 25. Create a dictionary containing student names and marks. Add a student, update marks, delete a student, search for a student, display all students, find highest marks, calculate the average.
# students = {"Sumit": 85, "Bhavesh": 90, "Rajesh": 78}
# new_name = input("Enter new student name to add: ")
# new_marks = int(input("Enter marks: "))
# students25[new_name25] = new_marks25
# update_name = input("Enter student name to update marks: ")
# if update_name in students
#     updated_marks= int(input("Enter updated marks: "))
#     students[update_name] = updated_marks
# delete_name = input("Enter student name to delete: ")
# if delete_name in students:
#     del students[delete_name]
# search_name = input("Enter student name to search: ")
# if search_name25 in students:
#     print("Marks of", search_name, ":", students[search_name])
# else:
#     print(search_name, "not found")
# print("All students:", students)
# if students:
#     highest_student = max(students, key=students.get)
#     print("Highest marks:", highest_student, "-", students[highest_student])
#     print("Average marks:", sum(students.values()) / len(students))

# # 26. Create a dictionary containing employee names and salaries. Find highest salary, lowest salary, average salary, employees earning more than ₹50,000.
# salaries26 = {"xyz": 45000, "abc": 60000, "pqr": 52000, "lmn": 38000}
# highest_salary_emp = max(salaries26, key=salaries26.get)
# lowest_salary_emp = min(salaries26, key=salaries26.get)
# average_salary26 = sum(salaries26.values()) / len(salaries26)
# print("Highest salary:", highest_salary_emp, "-", salaries26[highest_salary_emp])
# print("Lowest salary:", lowest_salary_emp, "-", salaries26[lowest_salary_emp])
# print("Average salary:", average_salary26)
# print("Employees earning more than 50000:")
# for name, salary in salaries26.items():
#     if salary > 50000:
#         print(name, "-", salary)

# # 27. Create a dictionary containing product names and quantities. Add a product, update quantity, delete a product, search for a product, display products with quantity below 10.
# products27 = {"Pen": 50, "Book": 5, "Bag": 20, "Bottle": 8}
# add_product27 = input("Enter new product name to add: ")
# add_qty27 = int(input("Enter quantity: "))
# products27[add_product27] = add_qty27
# update_product27 = input("Enter product name to update quantity: ")
# if update_product27 in products27:
#     update_qty27 = int(input("Enter updated quantity: "))
#     products27[update_product27] = update_qty27
# delete_product27 = input("Enter product name to delete: ")
# if delete_product27 in products27:
#     del products27[delete_product27]
# search_product27 = input("Enter product name to search: ")
# if search_product27 in products27:
#     print("Quantity of", search_product27, ":", products27[search_product27])
# else:
#     print(search_product27, "not found")
# print("Products with quantity below 10:")
# for product, qty in products27.items():
#     if qty < 10:
#         print(product, "-", qty)

# # 28. Create a dictionary containing names and phone numbers. Add contact, search contact, update contact, delete contact, display all contacts.
# contacts28 = {"name1": "999999999", "xyz": "999999999"}
# add_name28 = input("Enter new contact name: ")
# add_phone28 = input("Enter phone number: ")
# contacts28[add_name28] = add_phone28
# search_name28 = input("Enter contact name to search: ")
# if search_name28 in contacts28:
#     print("Phone number:", contacts28[search_name28])
# else:
#     print(search_name28, "not found")
# update_name28 = input("Enter contact name to update: ")
# if update_name28 in contacts28:
#     update_phone28 = input("Enter updated phone number: ")
#     contacts28[update_name28] = update_phone28
# delete_name28 = input("Enter contact name to delete: ")
# if delete_name28 in contacts28:
#     del contacts28[delete_name28]
# print("All contacts:", contacts28)

# # 29. Create a dictionary containing book IDs and book names. Add a book, search a book, remove a book, display all books, count total books.
# books29 = {1: "Python Basics", 2: "Data Structures", 3: "Algorithms"}
# add_id29 = int(input("Enter new book ID: "))
# add_name29 = input("Enter book name: ")
# books29[add_id29] = add_name29
# search_id29 = int(input("Enter book ID to search: "))
# if search_id29 in books29:
#     print("Book found:", books29[search_id29])
# else:
#     print("Book not found")
# remove_id= int(input("Enter book ID to remove: "))
# if remove_id in books:
#     del books[remove_id]
# print("All books:", books)
# print("Total books:", len(books))

# # 30. Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
# students_ = {"Adesh": "CS", "Bhavesh": "IT", "Parshwa": "CS", "Aryan": "CS", "Yash": "CS"}
# grouped_ = {}
# for name, department in students_.items():
#     grouped_.setdefault(department, []).append(name)
# print(grouped_)

#31.To take a list of words ,create a dictionary where key is word length and the value is list of words having that length
# words_=["python","cobra","my_relatives"]
# length_dict = {}
# for word in words_:
#     length_dict.setdefault(len(word), []).append(word)
# print(length_dict)

#32.To take list of integers and a target value,find two numbers whose sum is equal to target
# numbers = [2, 7, 11, 15, 3, 6]
# target = int(input("Enter target sum: "))
# seen = {}
# result = None
# for num in numbers:
#     complement = target - num
#     if complement in seen:
#         result = (complement, num)
#         break
#     seen[num] = True
# if result:
#     print("Pair found:", result)
# else:
#     print("No pair found")

'''34. Take a string, use a dictionary to find the first character that occurs more than once.'''
# string = input("Enter a string: ")
# char_count = {}
# first_repeating = None
# for char in string:
#     char_count[char] = char_count.get(char, 0) + 1
#     if char_count[char] == 2 and first_repeating is None:
#         first_repeating = char
# print("First repeating character:", first_repeating)

'''35. Accept a paragraph and create a dictionary where key = word length, value = number of words having that length.'''
# paragraph= input("Enter a paragraph: ")
# words = paragraph.split()
# length_count = {}
# for word in words:
#     length_count[len(word)] = length_count.get(len(word), 0) + 1
# print(length_count)