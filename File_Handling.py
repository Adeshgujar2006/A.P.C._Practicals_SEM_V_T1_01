#1.Python program to create a file named student.txt and write student's name,roll no.,semester & branch into the file
# def create_student_file():
#     with open("student.txt", "w") as file:
#         name = input("Enter student's name: ")
#         roll_no = input("Enter student's roll number: ")
#         semester = input("Enter student's semester: ")
#         branch = input("Enter student's branch: ")

#         file.write(f"Name: {name}\n")
#         file.write(f"Roll Number: {roll_no}\n")
#         file.write(f"Semester: {semester}\n")
#         file.write(f"Branch: {branch}\n")
#         file.write("\n")
#     print("Student information has been written to student.txt")
# create_student_file()

#2.Write a program to open a text file and display it's contents
# def display_contents():
#         with open("student.txt", "r") as file:
#             contents = file.read()
#             print("Contents of student.txt:")
#             print(contents)
# display_contents()

#3.To write a python program to additionally append student information to an existing file without deleting its previous contents
# def append_student_info():
#     with open("student.txt", "a") as file:
#         name = input("Enter student's name: ")
#         roll_no = input("Enter student's roll number: ")
#         semester = input("Enter student's semester: ")
#         branch = input("Enter student's branch: ")
#         file.write(f"Name: {name}\n")
#         file.write(f"Roll Number: {roll_no}\n")
#         file.write(f"Semester: {semester}\n")
#         file.write(f"Branch: {branch}\n")
#     print("Student information has been appended to student.txt")
# append_student_info()

#4.Write a program to read a text file line by line and display each line separately.
# def read_file_line_by_line():
#     with open("student.txt", "r") as file:
#         print("Reading student.txt line by line:")
#         for line in file:
#             print(line.strip())
# read_file_line_by_line()

#5.Write a program to count and display total no. of lines present in text file
# def count_lines():
#     with open("student.txt", "r") as file:
#         lines = file.readlines()
#         total_lines = len(lines)
#         print(f"Total number of lines in student.txt: {total_lines}")
# count_lines()

#6.Write a program to count total no. of words in the text file
# def count_words():
#     with open("student.txt", "r") as file:
#         contents = file.read()
#         words = contents.split()
#         total_words = len(words)
#         print(f"Total number of words in student.txt: {total_words}")
# count_words()

#7.program to count total no. of characters in a text file including whitespaces
# def count_characters():
#     with open("student.txt", "r") as file:
#         contents = file.read()
#         total_characters = len(contents)
#         print(f"Total number of characters in student.txt (including whitespaces): {total_characters}")
# count_characters()

#8.program to read a text file display its lines in reverse order
# def reverse_lines():
#     with open("student.txt", "r") as file:
#         lines = file.readlines()
#         print("Lines in student.txt in reverse order:")
#         for line in reversed(lines):
#             print(line.strip())
# reverse_lines()

#9.program to read a text files and count no. of vowels and consonants in a text file
# def count_vowels_consonants():
#     with open("student.txt", "r") as file:
#         contents = file.read().lower()
#         vowels = "aeiou"
#         consonants = "bcdfghjklmnpqrstvwxyz"
#         vowel_count = sum(1 for char in contents if char in vowels)
#         consonant_count = sum(1 for char in contents if char in consonants)
#         print(f"Total number of vowels in student.txt: {vowel_count}")
#         print(f"Total number of consonants in student.txt: {consonant_count}")
# count_vowels_consonants()

#10.	Read a text file and calculate the number of alphabets, digits, spaces, and special characters.
# def count_characters_types():
#     with open("student.txt", "r") as file:
#         contents = file.read()
#         alphabets = sum(1 for char in contents if char.isalpha())
#         digits = sum(1 for char in contents if char.isdigit())
#         spaces = sum(1 for char in contents if char.isspace())
#         special_characters = sum(1 for char in contents if not char.isalnum() and not char.isspace())
#         print(f"Total number of alphabets in student.txt: {alphabets}")
#         print(f"Total number of digits in student.txt: {digits}")
#         print(f"Total number of spaces in student.txt: {spaces}")
#         print(f"Total number of special characters in student.txt: {special_characters}")
# count_characters_types()

#11.	Read a text file and find the longest word present in the file.
# def longest_word():
    
#      with open("student.txt", "r") as file:
#         contents = file.read()
#         words = contents.split()
#         longest_word = max(words, key=len)
#         print(f"The longest word in student.txt is: {longest_word}")
# longest_word()

#12.	Read a text file and count how many times each word occurs. Display the result using a dictionary.
# def count_word_occurrences():
#     with open("student.txt", "r") as file:
#         contents = file.read().lower()
#         words = contents.split()
#         word_count = {}
        
#         for word in words:
#             word_count[word] = word_count.get(word, 0) + 1
        
#         print("Word occurrences in student.txt:")
#         print(word_count)
# count_word_occurrences()

#13.	Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
# def search_word_in_file():
#     word_to_search = input("Enter a word to search in student.txt: ").lower()
#     with open("student.txt", "r") as file:
#         lines = file.readlines()
#         occurrences = 0
#         line_numbers = []
        
#         for line_number, line in enumerate(lines, start=1):
#             if word_to_search in line.lower():
#                 occurrences += line.lower().count(word_to_search)
#                 line_numbers.append(line_number)
        
#         print(f"The word '{word_to_search}' occurs {occurrences} times in student.txt.")
#         if occurrences > 0:
#             print(f"It appears on the following line numbers: {line_numbers}")
#         else:
#             print("The word was not found in the file.")
# search_word_in_file()

#14.Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.
# def replace_word_in_file():
#     word_to_replace = input("Enter the word to replace: ")
#     replacement_word = input("Enter the replacement word: ")
    
#     with open("student.txt", "r") as file:
#         contents = file.read()
    
#     modified_contents = contents.replace(word_to_replace, replacement_word)
    
#     with open("student.txt", "w") as file:
#         file.write(modified_contents)
    
#     print(f"All occurrences of '{word_to_replace}' have been replaced with '{replacement_word}' in student.txt.")
# replace_word_in_file()

#15.	Read a Python source file and create another file after removing single-line comments.
# def read_create():
#     with open("student.txt", "r") as source_file:
#         lines = source_file.readlines()
    
#     with open("modified_student.txt", "w") as new_file:
#         for line in lines:
#             stripped_line = line.strip()
#             if not stripped_line.startswith("#"):
#                 new_file.write(line)
    
#     print("Single-line comments have been removed and saved to modified_student.txt.")
# read_create()

#16.	Read a text file and create another file containing the same text in uppercase.
# def create_uppercase_file():
#     with open("student.txt", "r") as source_file:
#         contents = source_file.read()
    
#     uppercase_contents = contents.upper()
    
#     with open("uppercase_student.txt", "w") as new_file:
#         new_file.write(uppercase_contents)
    
#     print("The contents of student.txt have been converted to uppercase and saved to uppercase_student.txt.")
# create_uppercase_file()

# 17.	Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to:
# •	Display all records. 
# •	Find the student with the highest marks. 
# •	Calculate average marks. 
# •	Display students who scored more than 80.

# def student_records():
#     with open("students.txt", "w") as file:
#         file.write("RollNo,Name,Marks\n")
#         file.write("01,Adesh,95\n")
#         file.write("05,Yash,92\n")
#         file.write("10,Parth,98\n")

#     print("\nStudent Records:")
#     with open("students.txt", "r") as file:
#         print(file.read())

#     highest = None
#     total = 0
#     count = 0

#     with open("students.txt", "r") as file:
#         next(file)
#         for line in file:
#             roll, name, marks = line.strip().split(",")
#             marks = int(marks)
#             total += marks
#             count += 1

#             if highest is None or marks > highest[2]:
#                 highest = (roll, name, marks)

#             if marks > 80:
#                 print("Above 80:", name, marks)

#     print("Highest Marks:", highest[1], highest[2])
#     print("Average Marks:", total / count)
# student_records()


# 18.	Store employee ID, name, department, and salary in a file. Write functions to: 
# •	Display all employees. 
# •	Find the highest-paid employee. 
# •	Calculate average salary. 
# •	Display employees earning above a given salary.

# def employee_records():
#     with open("employees.txt", "w") as file:
#         file.write("EmployeeID,Name,Department,Salary\n")
#         file.write("201,Adesh,IT,60000\n")
#         file.write("202,Yash,HR,45000\n")
#         file.write("203,Parth,Finance,75000\n")

#     print("\nEmployee Records:")
#     with open("employees.txt", "r") as file:
#         print(file.read())

#     highest = None
#     total = 0
#     count = 0
#     amount = float(input("Enter salary: "))

#     with open("employees.txt", "r") as file:
#         next(file)

#         for line in file:
#             emp_id, name, dept, salary = line.strip().split(",")
#             salary = float(salary)
#             total += salary
#             count += 1

#             if highest is None or salary > highest[3]:
#                 highest = (emp_id, name, dept, salary)

#             if salary > amount:
#                 print("Above Given Salary:", name, salary)

#     print("Highest Paid Employee:", highest[1], highest[3])
#     print("Average Salary:", total / count)
# employee_records()


#19.Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
# def attendance_records():
#     with open("attendance.txt", "w") as file:
#         file.write("RollNo,Name,Present,Total\n")
#         file.write("101,Adesh,42,50\n")
#         file.write("102,Pratham,35,50\n")
#         file.write("103,Yash,48,50\n")

#     with open("attendance.txt", "r") as file:
#         next(file)

#         for line in file:
#             roll, name, present, total = line.strip().split(",")
#             percentage = (int(present) / int(total)) * 100

#             print(name, ":", percentage, "%")

#             if percentage < 75:
#                 print("Below 75%:", name)
# attendance_records()


# 20.	Store deposits and withdrawals in a file. Read the file and calculate: 
# •	Total deposits 
# •	Total withdrawals 
# •	Final balance 
# •	Largest transaction

# def transactions():
#     with open("transactions.txt", "w") as file:
#         file.write("Transaction,Amount\n")
#         file.write("Deposit,10000\n")
#         file.write("Withdrawal,2500\n")
#         file.write("Deposit,5000\n")
#         file.write("Withdrawal,1000\n")

#     deposits = 0
#     withdrawals = 0
#     balance = 0
#     largest = 0

#     with open("transactions.txt", "r") as file:
#         next(file)

#         for line in file:
#             transaction, amount = line.strip().split(",")
#             amount = float(amount)

#             if transaction == "Deposit":
#                 deposits += amount
#                 balance += amount
#             else:
#                 withdrawals += amount
#                 balance -= amount

#             if amount > largest:
#                 largest = amount

#     print("Total Deposits:", deposits)
#     print("Total Withdrawals:", withdrawals)
#     print("Final Balance:", balance)
#     print("Largest Transaction:", largest)
# transactions()


#21.	Maintain book records containing book ID, title, author, and availability status. Implement operations to: 
# •	Add a book. 
# •	Search for a book. 
# •	Issue a book. 
# •	Return a book. 
# •	Display available books.

# def add_book():
#     book_id = input("Enter Book ID: ")
#     title = input("Enter Title: ")
#     author = input("Enter Author: ")

#     with open("books.txt", "a") as file:
#         file.write(f"{book_id},{title},{author},Available\n")

#     print("Book added successfully")


# def search_book():
#     book_id = input("Enter Book ID: ")

#     with open("books.txt", "r") as file:
#         for line in file:
#             bid, title, author, status = line.strip().split(",")

#             if bid == book_id:
#                 print("Book ID:", bid)
#                 print("Title:", title)
#                 print("Author:", author)
#                 print("Status:", status)
#                 return

#     print("Book not found")


# def issue_book():
#     book_id = input("Enter Book ID: ")

#     with open("books.txt", "r") as file:
#         books = file.readlines()

#     with open("books.txt", "w") as file:
#         for line in books:
#             bid, title, author, status = line.strip().split(",")

#             if bid == book_id:
#                 if status == "Available":
#                     status = "Issued"
#                     print("Book issued successfully")
#                 else:
#                     print("Book already issued")

#             file.write(f"{bid},{title},{author},{status}\n")


# def return_book():
#     book_id = input("Enter Book ID: ")

#     with open("books.txt", "r") as file:
#         books = file.readlines()

#     with open("books.txt", "w") as file:
#         for line in books:
#             bid, title, author, status = line.strip().split(",")

#             if bid == book_id:
#                 status = "Available"
#                 print("Book returned successfully")

#             file.write(f"{bid},{title},{author},{status}\n")


# def available_books():
#     print("\nAvailable Books:")

#     with open("books.txt", "r") as file:
#         for line in file:
#             bid, title, author, status = line.strip().split(",")

#             if status == "Available":
#                 print(bid, title, author)


# def book_management():
#     while True:
#         print("\n1. Add Book")
#         print("2. Search Book")
#         print("3. Issue Book")
#         print("4. Return Book")
#         print("5. Display Available Books")
#         print("6. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             add_book()
#         elif choice == "2":
#             search_book()
#         elif choice == "3":
#             issue_book()
#         elif choice == "4":
#             return_book()
#         elif choice == "5":
#             available_books()
#         elif choice == "6":
#             break
#         else:
#             print("Invalid choice")
# book_management()

#22.Read the contents of two text files and create a third file containing the contents of both files.
# def combine_files():
#     with open("file1.txt", "r") as file1:
#         content1 = file1.read()

#     with open("file2.txt", "r") as file2:
#         content2 = file2.read()

#     with open("file3.txt", "w") as file3:
#         file3.write(content1)
#         file3.write("\n")
#         file3.write(content2)

#     print("Files combined successfully")
# combine_files()



#23.	Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.
# def compare_files():
#     with open("student.txt", "r") as file1:
#         lines1 = file1.readlines()

#     with open("sample.txt", "r") as file2:
#         lines2 = file2.readlines()

#     if lines1 == lines2:
#         print("Both files are identical")
#         return

#     print("Files are different")

#     minimum = min(len(lines1), len(lines2))

#     for i in range(minimum):
#         if lines1[i] != lines2[i]:
#             print("First different line:", i + 1)
#             print("File 1:", lines1[i].strip())
#             print("File 2:", lines2[i].strip())
#             return

#     print("First different line:", minimum + 1)
# compare_files()