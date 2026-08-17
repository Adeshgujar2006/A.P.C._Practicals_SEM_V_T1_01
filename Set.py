# # 1. Write a Python program to create a set containing five integers and display all its elements.
# set1 = {10, 20, 30, 40, 50}
# print(set1)

# # 2. Create a list containing duplicate values. Convert the list into a set and display the resulting set.
# list = [1, 2, 2, 3, 4, 4, 5]
# set = set(list)
# print(set)

# 3. Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
# fruits3 = {"Apple", "Banana", "Mango", "Grapes", "Orange"}
# fruits3.add("Papaya")
# fruits3.add("Jackfruit")
# print(fruits3)

# 4. Create a set of numbers and remove a specified number from the set.
# numbers4 = {10, 20, 30, 40, 50}
# num4 = int(input("Enter number to remove: "))
# if num4 in numbers4:
#     numbers4.remove(num4)
# print(numbers4)

# # 5. Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
# students5 = {"Suman", "Parshwnath", "animesh", "adesh"}
# name5 = input("Enter student name to check: ")
# if name5 in students5:
#     print(name5, "exists in the set")
# else:
#     print(name5, "does not exist in the set")

# # 6. Create a set of cities and determine the total number of cities using an appropriate function.
# cities6 = {"Mumbai", "Delhi", "Pune", "Chennai"}
# print("Total cities:", len(cities6))

# # 7. Create a set of programming languages and display each language using a for loop.
# languages7 = {"Python", "Java", "C++", "JavaScript"}
# for language in languages7:
#     print(language)

# # 8. Create a list containing duplicate numbers, use a set to remove the duplicates.
# list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# Set_=set(list)
# print(Set_)

# # 9. Create two sets of integers and find their union.
# set9_a = {1, 2, 3, 4}
# set9_b = {3, 4, 5, 6}
# print(set9_a | set9_b)

# # 10. Create two sets and find the elements common to both sets.
# set10_a = {1, 2, 3, 4}
# set10_b = {3, 4, 5, 6}
# print(set10_a & set10_b)

# # 11. Create two sets and find elements present in the first set but not the second, and in the second but not the first.
# set11_a = {1, 2, 3, 4}
# set11_b = {3, 4, 5, 6}
# print("In first but not second:", set11_a - set11_b)
# print("In second but not first:", set11_b - set11_a)

# # 12. Create two sets of numbers and find the elements that are present in either set but not in both.
# set12_a = {1, 2, 3, 4}
# set12_b = {3, 4, 5, 6}
# print(set12_a ^ set12_b)

# # 13. Create two sets and determine whether the first set is a subset of the second set.
# set13_a = {1, 2}
# set13_b = {1, 2, 3, 4}
# print(set13_a.issubset(set13_b))

# # 14. Create two sets and determine whether the first set is a superset of the second set.
# set14_a = {1, 2, 3, 4}
# set14_b = {1, 2}
# print(set14_a.issuperset(set14_b))

# # 15. Write a program to determine whether two sets have no elements in common.
# set15_a = {1, 2, 3}
# set15_b = {4, 5, 6}
# print(set15_a.isdisjoint(set15_b))

# # 16. Create two sets and check whether they are equal.
# set16_a = {1, 2, 3}
# set16_b = {3, 2, 1}
# print(set16_a == set16_b)

# # 17. Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
# subjects_student1 = {"Maths", "Physics", "Chemistry"}
# subjects_student2 = {"CC", "APC", "AJT"}
# print(subjects_student1 & subjects_student2)

# 18. Accept a sentence from the user and use a set to display all unique words.
# sentence18 = input("Enter a sentence: ")
# unique_words18 = set(sentence18.split())
# print(unique_words18)

# # 19. Create two sets: students present in the morning session and afternoon session.
# morning19 = {"adesh", "rajesh", "xyz", "lmn"}
# afternoon19 = {"vikas", "animesh", "abc", "pqr"}
# print("Both sessions:", morning19 & afternoon19)
# print("Only morning:", morning19 - afternoon19)
# print("Only afternoon:", afternoon19 - morning19)
# print("At least one session:", morning19 | afternoon19)

# # 20. Create sets representing students enrolled in Python and Java. Find students enrolled in both courses and students enrolled in only one course.
# python_students20 = {"Adesh", "Arshad", "Harshal"}
# java_students20 = {"Arshad", "Harshal", "Adesh"}
# print("Both courses:", python_students20 & java_students20)
# print("Only one course:", python_students20 ^ java_students20)

# # 21. Create two sets representing technical skills of two employees. Find common skills, unique skills, and all available skills.
# skills_emp1 = {"Python", "SQL", "Excel"}
# skills_emp2 = {"SQL", "Java", "Excel", "AWS"}
# print("Common skills:", skills_emp1 & skills_emp2)
# print("Unique to Employee 1:", skills_emp1 - skills_emp2)
# print("Unique to Employee 2:", skills_emp2 - skills_emp1)
# print("All available skills:", skills_emp1 | skills_emp2)

# # 22. Create a set containing available books and another set containing requested books. Determine which requested books are available.
# available_books = {"Python Basics", "Data Structures", "Algorithms", "AI Fundamentals"}
# requested_books = {"Data Structures", "Machine Learning", "AI Fundamentals"}
# print("Available requested books:", requested_books & available_books)

# # 23. Store visitor IDs from two different days in separate sets. Determine unique visitors, returning visitors, and visitors from only one day.
# day1_visitors = {101, 102, 103, 104}
# day2_visitors = {103, 107, 105, 106}
# print("Unique visitors across both days:", day1_visitors | day2_visitors)
# print("Returning visitors:", day1_visitors & day2_visitors)
# print("Only first day:", day1_visitors - day2_visitors)
# print("Only second day:", day2_visitors - day1_visitors)

# # 24. Create sets representing products belonging to different categories. Find products that belong to both categories.
# category1_products24 = {"Laptop", "Mouse", "Keyboard"}
# category2_products24 = {"Mouse", "Monitor", "Keyboard"}
# print(category1_products24 & category2_products24)

# 25. Represent the friends of two users using sets. Find mutual friends, unique friends, and total unique friends.
# friends_1 = {"Adesh", "Bhavesh", "Shreyash"}
# friends_2 = {"Shivam", "Yash", "Adesh"}
# print("Mutual friends:", friends_1 & friends_2)
# print("Unique to User 1:", friends_1 - friends_2)
# print("Unique to User 2:", friends_2 - friends_1)
# print("Total unique friends:", friends_1 | friends_2)