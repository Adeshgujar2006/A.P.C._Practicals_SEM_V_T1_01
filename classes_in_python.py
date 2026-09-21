#1.Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.
# class Student:
#     def __init__(self,roll_no,name,marks):
#         self.roll_no=roll_no
#         self.name=name
#         self.marks=marks
#     def percentage(self):
#         return sum(self.marks)/len(self.marks)
#     def display(self):
#         print("Roll no.:",self.roll_no)
#         print("Name:",self.name)
#         print("Percentage is:",self.percentage(),"%")
#         print()
# s1=Student(1,"Adesh",[90,85,70,95,90])
# s2=Student(93,"Shivam",[89,89,87,98,90])
# s1.display()
# s2.display()

#2.	Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.
# class Employee:
#     def __init__(self,emp_id,name,basic_salary):
#         self.emp_id=emp_id
#         self.name=name
#         self.basic_salary=basic_salary
#     def HRA(self):
#         return 10/100*self.basic_salary
#     def DA(self):
#         return 15/100*self.basic_salary
#     def Gross_salary(self):
#         return self.basic_salary+self.HRA()+self.DA()
#     def display(self):
#         print("Employee ID:",self.emp_id)
#         print("Name:",self.name)
#         print("Gross Salary of the employee is:",self.Gross_salary())
# emp1=Employee("H1253","Adesh",230000)
# emp2=Employee("H1254","Bhavesh",320000)
# emp1.display()
# emp2.display()

# 3. Create a class Rectangle with attributes length and breadth. Define methods to calculate area and
# perimeter.

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

# r = Rectangle(10, 5)

# print("Area:", r.area())
# print("Perimeter:", r.perimeter())


# 4. Create a class Circle with an attribute radius. Define methods to calculate the area and
# circumference of the circle.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius

# c = Circle(7)

# print("Area:", c.area())
# print("Circumference:", c.circumference())


# 5. Create a class Book containing book_id, title, author, and price. Create objects for three books
# and display their information.

# class Book:
#     def __init__(self, book_id, title, author, price):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Book ID:", self.book_id)fdswq  
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)
#         print()

# b1 = Book(1, "Atomic Habits", "James Clear", 500)
# b2 = Book(2, "Data Structures", "Seymour Lipschutz", 200)
# b3 = Book(3, "Machine Learning", "David Miller", 750)

# b1.display()
# b2.display()
# b3.display()


# 6. Create a class ElectricityBill containing consumer number, consumer name, and units consumed.
# Define a method to calculate the electricity bill according to different unit slabs.

# class ElectricityBill:
#     def __init__(self, consumer_no, consumer_name, units):
#         self.consumer_no = consumer_no
#         self.consumer_name = consumer_name
#         self.units = units

#     def calculate_bill(self):
#         units = self.units

#         if units <= 100:
#             bill = units * 1.5
#         elif units <= 200:
#             bill = 100 * 1.5 + (units - 100) * 2.5
#         elif units <= 300:
#             bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
#         else:
#             bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 5

#         return bill

#     def display(self):
#         print("Consumer Number:", self.consumer_no)
#         print("Consumer Name:", self.consumer_name)
#         print("Units Consumed:", self.units)
#         print("Electricity Bill:", self.calculate_bill())

# eb = ElectricityBill(1001, "Adesh", 250)
# eb.display()


# 7. Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to
# display specifications and calculate the price after discount.

# class MobilePhone:
#     def __init__(self, brand, model, storage, price):
#         self.brand = brand
#         self.model = model
#         self.storage = storage
#         self.price = price

#     def display_specs(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Storage:", self.storage)
#         print("Price:", self.price)

#     def discounted_price(self, discount):
#         return self.price - (self.price * discount / 100)

# phone = MobilePhone("Samsung", "Galaxy A36", "256 GB", 30000)

# phone.display_specs()
# print("Price after 10% discount:", phone.discounted_price(10))


# 8. Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define
# methods to display patient information and calculate the total bill.

# class Patient:
#     def __init__(self, patient_id, name, age, disease, consultation_fee):
#         self.patient_id = patient_id
#         self.name = name
#         self.age = age
#         self.disease = disease
#         self.consultation_fee = consultation_fee

#     def display(self):
#         print("Patient ID:", self.patient_id)
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Disease:", self.disease)
#         print("Consultation Fee:", self.consultation_fee)

#     def total_bill(self, medicine_fee=0, test_fee=0):
#         return self.consultation_fee + medicine_fee + test_fee

# p = Patient(101, "Adesh", 20, "Fever", 500)

# p.display()
# print("Total Bill:", p.total_bill(800, 1000))


# 9. Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Create an object of the class and implement the operations through a menu-driven program.

# class ATM:
#     def __init__(self, account_no, name, balance):
#         self.account_no = account_no
#         self.name = name
#         self.balance = balance

#     def check_balance(self):
#         print("Balance:", self.balance)

#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount deposited successfully.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Amount withdrawn successfully.")
#         else:
#             print("Insufficient balance.")

#     def account_details(self):
#         print("Account Number:", self.account_no)
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)

# atm = ATM(1125532553, "Adesh", 10000)

# while True:
#     print("\n1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Display Account Details")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         atm.check_balance()

#     elif choice == 2:
#         amount = float(input("Enter amount to deposit: "))
#         atm.deposit(amount)

#     elif choice == 3:
#         amount = float(input("Enter amount to withdraw: "))
#         atm.withdraw(amount)

#     elif choice == 4:
#         atm.account_details()

#     elif choice == 5:
#         print("Thank you.")
#         break

#     else:
#         print("Invalid choice.")


# 10. Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement
# methods to rent and return a vehicle and calculate rental charges based on the number of days.

# class Vehicle:
#     def __init__(self, vehicle_no, model, rental_rate):
#         self.vehicle_no = vehicle_no
#         self.model = model
#         self.rental_rate = rental_rate
#         self.available = True
#     def rent(self):
#         if self.available:
#             self.available = False
#             print("Vehicle rented successfully.")
#         else:
#             print("Vehicle is not available.")
#     def return_vehicle(self):
#         self.available = True
#         print("Vehicle returned successfully.")
#     def rental_charges(self, days):
#         return self.rental_rate * days
#     def display(self):
#         print("Vehicle Number:", self.vehicle_no)
#         print("Model:", self.model)
#         print("Rental Rate:", self.rental_rate)
#         print("Available:", self.available)
# v = Vehicle("MH09BA4598", "Tata Harrier", 1500)
# v.display()
# v.rent()
# print("Rental Charges for 3 days:", v.rental_charges(5))
# v.return_vehicle()

#11.Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.

# class ShoppingCart:
#     def __init__(self, customer_name, cart_id):
#         self.customer_name = customer_name
#         self.cart_id = cart_id
#         self.products = {}
#     def add_product(self, name, price):
#         self.products[name] = price
#     def remove_product(self, name):
#         if name in self.products:
#             del self.products[name]
#         else:
#             print("Product not found.")
#     def total_bill(self):
#         return sum(self.products.values())
#     def display(self):
#         print("Customer Name:", self.customer_name)
#         print("Cart ID:", self.cart_id)
#         print("Products:", self.products)
#         print("Total Bill:", self.total_bill())
#     def __del__(self):
#         print("Shopping cart object destroyed.")
# cart = ShoppingCart("Adesh", 101)
# cart.add_product("Laptop", 50000)
# cart.add_product("Mouse", 1000)
# cart.add_product("Keyboard", 2000)
# cart.remove_product("Keyboard")
# cart.display()
        

#12.Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.

# class FoodOrder:
#     def __init__(self, order_ID, cus_name, food_item, quantity, price):
#         self.order_ID = order_ID
#         self.cus_name = cus_name
#         self.food_item = food_item
#         self.quantity = quantity
#         self.price = price
#     def total_bill(self):
#         subtotal = self.quantity * self.price
#         tax = subtotal * 0.18
#         return subtotal + tax
#     def display(self):
#         subtotal = self.quantity * self.price
#         gst = subtotal * 0.18
#         print("Order ID:", self.order_ID)
#         print("Customer Name:", self.cus_name)
#         print("Food Item:", self.food_item)
#         print("Quantity:", self.quantity)
#         print("Price:", self.price)
#         print("GST:", gst)
#         print("Total Bill:", self.total_bill())
#     def __del__(self):
#         print("Order completed.")
# order = FoodOrder(101, "Adesh", "Veg Biryani", 2, 160)
# order.display()


# 13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to
# initialize the details. Define methods to calculate total, percentage, and grade. Implement a
# destructor to display a suitable message.

# class StudentResult:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def total(self):
#         return sum(self.marks)

#     def percentage(self):
#         return self.total() / 5
#     def grade(self):
#         percentage = self.percentage()
#         if percentage >= 90:
#             return "A+"
#         elif percentage >= 80:
#             return "A"
#         elif percentage >= 70:
#             return "B"
#         elif percentage >= 60:
#             return "C"
#         elif percentage >= 50:
#             return "D"
#         else:
#             return "F"
#     def display(self):
#         print("Student Name:", self.name)
#         print("Total:", self.total())
#         print("Percentage:", self.percentage(), "%")
#         print("Grade:", self.grade())
#     def __del__(self):
#         print("Student result object destroyed.")
# result = StudentResult("Adesh", [85, 90, 78, 88, 92])
# result.display()




