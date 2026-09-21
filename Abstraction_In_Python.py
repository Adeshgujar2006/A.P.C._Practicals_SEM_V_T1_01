# 1. Create an abstract class Shape with an abstract method area().
# Derive Circle, Rectangle, and Triangle classes and implement the area()
# method for each shape. Create objects of the derived classes and display their areas.

from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# for shape in [Circle(5), Rectangle(10, 5), Triangle(10, 6)]:
#     print(shape.area())


# 2. Create an abstract class Vehicle with abstract methods start() and stop().
# Derive Car, Bike, and Bus classes and implement these methods.

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike started")

#     def stop(self):
#         print("Bike stopped")

# class Bus(Vehicle):
#     def start(self):
#         print("Bus started")

#     def stop(self):
#         print("Bus stopped")

# for vehicle in [Car(), Bike(), Bus()]:
#     vehicle.start()
#     vehicle.stop()

# 3. Create an abstract class BankAccount with abstract methods deposit()
# and withdraw(). Derive SavingsAccount and CurrentAccount and implement
# the required operations.

# class BankAccount(ABC):
#     def __init__(self, balance):
#         self.balance = balance

#     @abstractmethod
#     def deposit(self, amount):
#         pass

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

# class SavingsAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount

# class CurrentAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount

# s = SavingsAccount(10000)
# s.deposit(2000)
# s.withdraw(3000)
# print("Savings Balance:", s.balance)

# c = CurrentAccount(10000)
# c.deposit(5000)
# c.withdraw(2000)
# print("Current Balance:", c.balance)


# 4. Create an abstract class FoodOrder with abstract methods calculate_bill()
# and delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and
# implement the methods appropriately.

# class FoodOrder(ABC):
#     @abstractmethod
#     def calculate_bill(self):
#         pass

#     @abstractmethod
#     def delivery_charge(self):
#         pass


# class RestaurantOrder(FoodOrder):
#     def __init__(self, amount):
#         self.amount = amount

#     def calculate_bill(self):
#         return self.amount

#     def delivery_charge(self):
#         return 0


# class HomeDeliveryOrder(FoodOrder):
#     def __init__(self, amount):
#         self.amount = amount

#     def calculate_bill(self):
#         return self.amount

#     def delivery_charge(self):
#         return 50


# for order in [RestaurantOrder(500), HomeDeliveryOrder(500)]:
#     print(order.calculate_bill() + order.delivery_charge())


# 5. Create an abstract class Patient with abstract methods calculate_bill()
# and treatment(). Derive InPatient, OutPatient, and EmergencyPatient classes
# and implement the methods according to the patient type.

# class Patient(ABC):
#     @abstractmethod
#     def calculate_bill(self):
#         pass

#     @abstractmethod
#     def treatment(self):
#         pass


# class InPatient(Patient):
#     def calculate_bill(self):
#         return 5000

#     def treatment(self):
#         return "Hospital admission and treatment"


# class OutPatient(Patient):
#     def calculate_bill(self):
#         return 1000

#     def treatment(self):
#         return "Consultation and medicine"


# class EmergencyPatient(Patient):
#     def calculate_bill(self):
#         return 10000

#     def treatment(self):
#         return "Emergency treatment"


# for p in [InPatient(), OutPatient(), EmergencyPatient()]:
#     print(p.treatment(), p.calculate_bill())


# 6. Create an abstract class Transport with an abstract method calculate_fare(distance).
# Implement subclasses Bus, Train, Taxi, and Flight. Calculate the fare according
# to the transportation type.

# class Transport(ABC):
#     @abstractmethod
#     def calculate_fare(self, distance):
#         pass


# class Bus(Transport):
#     def calculate_fare(self, distance):
#         return distance * 2


# class Train(Transport):
#     def calculate_fare(self, distance):
#         return distance * 1.5


# class Taxi(Transport):
#     def calculate_fare(self, distance):
#         return distance * 15


# class Flight(Transport):
#     def calculate_fare(self, distance):
#         return distance * 10


# for t in [Bus(), Train(), Taxi(), Flight()]:
#     print(t.calculate_fare(100))


# 7. Create an abstract class Question with an abstract method evaluate_answer().
# Derive MCQQuestion, TrueFalseQuestion, and DescriptiveQuestion.
# Implement answer evaluation for each question type.

# class Question(ABC):
#     @abstractmethod
#     def evaluate_answer(self, answer):
#         pass


# class MCQQuestion(Question):
#     def evaluate_answer(self, answer):
#         return answer == "B"


# class TrueFalseQuestion(Question):
#     def evaluate_answer(self, answer):
#         return answer == "True"


# class DescriptiveQuestion(Question):
#     def evaluate_answer(self, answer):
#         return len(answer) >= 20


# print(MCQQuestion().evaluate_answer("B"))
# print(TrueFalseQuestion().evaluate_answer("True"))
# print(DescriptiveQuestion().evaluate_answer("Python is an object oriented language."))


# 8. Create an abstract class Authentication with an abstract method authenticate().
# Implement the method using Password authentication, OTP authentication,
# and Biometric authentication. Demonstrate abstraction by interacting with
# objects through the abstract interface.

# class Authentication(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass


# class PasswordAuthentication(Authentication):
#     def authenticate(self):
#         print("Authenticated using password")


# class OTPAuthentication(Authentication):
#     def authenticate(self):
#         print("Authenticated using OTP")


# class BiometricAuthentication(Authentication):
#     def authenticate(self):
#         print("Authenticated using biometric")


# for auth in [
#     PasswordAuthentication(),
#     OTPAuthentication(),
#     BiometricAuthentication()
# ]:
#     auth.authenticate()


# 9. Create an abstract class CloudStorage with abstract methods upload_file(),
# download_file(), and delete_file(). Create subclasses representing different
# storage services and implement the operations.

# class CloudStorage(ABC):
#     @abstractmethod
#     def upload_file(self):
#         pass

#     @abstractmethod
#     def download_file(self):
#         pass

#     @abstractmethod
#     def delete_file(self):
#         pass

# class GoogleDrive(CloudStorage):
#     def upload_file(self):
#         print("File uploaded to Google Drive")

#     def download_file(self):
#         print("File downloaded from Google Drive")

#     def delete_file(self):
#         print("File deleted from Google Drive")

# class OneDrive(CloudStorage):
#     def upload_file(self):
#         print("File uploaded to OneDrive")

#     def download_file(self):
#         print("File downloaded from OneDrive")

#     def delete_file(self):
#         print("File deleted from OneDrive")

# for storage in [GoogleDrive(), OneDrive()]:
#     storage.upload_file()
#     storage.download_file()
#     storage.delete_file()


# 10. Create an abstract class Appointment with abstract methods
# book_appointment() and calculate_fee(). Derive GeneralAppointment,
# SpecialistAppointment, and EmergencyAppointment.

# class Appointment(ABC):
#     @abstractmethod
#     def book_appointment(self):
#         pass

#     @abstractmethod
#     def calculate_fee(self):
#         pass

# class GeneralAppointment(Appointment):
#     def book_appointment(self):
#         print("General appointment booked")

#     def calculate_fee(self):
#         return 500

# class SpecialistAppointment(Appointment):
#     def book_appointment(self):
#         print("Specialist appointment booked")

#     def calculate_fee(self):
#         return 1000

# class EmergencyAppointment(Appointment):
#     def book_appointment(self):
#         print("Emergency appointment booked")

#     def calculate_fee(self):
#         return 2000

# for appointment in [
#     GeneralAppointment(),
#     SpecialistAppointment(),
#     EmergencyAppointment()
# ]:
#     appointment.book_appointment()
#     print("Fee:", appointment.calculate_fee())