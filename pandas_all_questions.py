import pandas as pd

# Question 1
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.
students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Python": [85, 72, 90, 68, 78],
    "DBMS": [80, 75, 88, 70, 82],
    "Mathematics": [90, 70, 92, 65, 76]
}

df = pd.DataFrame(students)
print(df)
df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)
print(df)
print(df[df["Average"] > 75])


# Question 2
# Create an employee DataFrame and display salary above 50,000, average salary, highest salary, and employee with highest experience.
employees = {
    "Employee_ID": [201, 202, 203, 204, 205],
    "Employee_Name": ["Arun", "Neha", "Vijay", "Pooja", "Kiran"],
    "Department": ["CSE", "IT", "HR", "CSE", "Finance"],
    "Salary": [55000, 48000, 62000, 51000, 45000],
    "Experience": [5, 3, 8, 6, 2]
}

df = pd.DataFrame(employees)
print(df[df["Salary"] > 50000])
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print(df.loc[df["Experience"].idxmax()])


# Question 3
# Create a product DataFrame, calculate Total Amount = Price × Quantity, and find the product having the highest total sales.
products = {
    "Product_ID": [301, 302, 303, 304, 305],
    "Product_Name": ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories"],
    "Price": [60000, 25000, 30000, 15000, 2000],
    "Quantity": [2, 5, 3, 4, 10]
}

df = pd.DataFrame(products)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print(df)
print(df.loc[df["Total_Amount"].idxmax()])


# Question 4
# Create a patient DataFrame and display patients above 60, average and maximum medical charges, and patients with charges above 50,000.
patients = {
    "Patient_ID": [401, 402, 403, 404, 405],
    "Patient_Name": ["Ramesh", "Suresh", "Anita", "Meena", "Raj"],
    "Age": [65, 45, 72, 58, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [60000, 15000, 85000, 30000, 55000]
}

df = pd.DataFrame(patients)
print(df[df["Age"] > 60])
print("Average Medical Charge:", df["Medical_Charges"].mean())
print("Maximum Medical Charge:", df["Medical_Charges"].max())
print(df[df["Medical_Charges"] > 50000])


# Question 5
# Create an order DataFrame, calculate Final Amount = Quantity × Price − Discount, and display all orders, orders above 5,000, highest-value order, and average order value.
orders = {
    "Order_ID": [501, 502, 503, 504, 505],
    "Customer": ["Amit", "Neha", "Ravi", "Pooja", "Kiran"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard"],
    "Quantity": [1, 2, 3, 2, 5],
    "Price": [60000, 25000, 30000, 15000, 2000],
    "Discount": [2000, 1000, 1500, 500, 200]
}

df = pd.DataFrame(orders)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print(df)
print(df[df["Final_Amount"] > 5000])
print(df.loc[df["Final_Amount"].idxmax()])
print("Average Order Value:", df["Final_Amount"].mean())


# Question 6
# Create an attendance DataFrame, calculate Attendance Percentage, and display students with attendance below 75%.
attendance = {
    "Student_ID": [601, 602, 603, 604, 605],
    "Name": ["Amit", "Sneha", "Rohan", "Priya", "Kunal"],
    "Department": ["CSE", "IT", "CSE", "AIML", "IT"],
    "Total_Classes": [100, 100, 90, 120, 110],
    "Classes_Attended": [85, 70, 60, 100, 75]
}

df = pd.DataFrame(attendance)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100
print(df)
print(df[df["Attendance_Percentage"] < 75])


# Question 7
# Create a retail sales DataFrame, calculate Total Sales, display products with sales above 10,000, maximum sales, average sales, and perform operations on a student marks Series.
sales = {
    "Product_ID": [701, 702, 703, 704, 705],
    "Product_Name": ["Laptop", "Mobile", "Tablet", "TV", "Headphones"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories"],
    "Price": [60000, 25000, 30000, 45000, 3000],
    "Quantity": [2, 5, 3, 1, 10]
}

df = pd.DataFrame(sales)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print(df[df["Total_Sales"] > 10000])
print(df.loc[df["Total_Sales"].idxmax()])
print("Average Sales:", df["Total_Sales"].mean())

student_marks = {
    "Amit": 85,
    "Rahul": 72,
    "Sneha": 91,
    "Priya": 68,
    "Rohan": 78
}

series = pd.Series(student_marks)
print(series)
print(series["Amit"])
print("Maximum Marks:", series.max())
print("Minimum Marks:", series.min())
print("Average Marks:", series.mean())
print(series[series > 75])


# Question 8
# Create an employee salary Series and find highest salary, lowest salary, average salary, and employees earning above 50,000.
employee_salaries = {
    "Amit": 55000,
    "Neha": 48000,
    "Vijay": 62000,
    "Pooja": 51000,
    "Kiran": 45000
}

series = pd.Series(employee_salaries)
print(series)
print("Highest Salary:", series.max())
print("Lowest Salary:", series.min())
print("Average Salary:", series.mean())
print(series[series > 50000])


# Question 9
# Create a product price Series, display prices, increase every price by 10%, find the most expensive product, and display products costing more than 1,000.
product_prices = {
    "Laptop": 60000,
    "Mobile": 25000,
    "Tablet": 30000,
    "Monitor": 15000,
    "Keyboard": 2000
}

series = pd.Series(product_prices)
print(series)
series = series * 1.10
print(series)
print("Most Expensive Product:", series.idxmax())
print(series[series > 1000])


# Question 10
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.0
patient_ages = {
    1001: 65,
    1002: 45,
    1003: 72,
    1004: 58,
    1005: 68
}

series = pd.Series(patient_ages)
print("Average Age:", series.mean())
print("Oldest Patient:", series.idxmax(), series.max())
print("Youngest Patient:", series.idxmin(), series.min())
print(series[series > 60])


# Question 11
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.1
attendance_percentages = {
    "Amit": 85,
    "Rahul": 72,
    "Sneha": 95,
    "Priya": 68,
    "Rohan": 92
}

series = pd.Series(attendance_percentages)
print("Average Attendance:", series.mean())
print(series[series < 75])
print(series[series > 90])
print("Highest Attendance:", series.max())


# Question 12
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.2
df = pd.read_csv("students.csv")
print(df.head())
print(df.tail())

subjects = ["Python", "DBMS", "Maths"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

print(df)
print(df[df["Average"] > 75])
print(df.loc[df["Average"].idxmax()])
print(df[subjects].mean())


# Question 13
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.3
df = pd.read_csv("employees.csv")
print(df[df["Department"] == "CSE"])
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print(df[df["Salary"] > 50000])
print(df.groupby("Department")["Salary"].mean())


# Question 14
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.4
df = pd.read_csv("patients.csv")
print(df[df["Age"] > 60])
print("Average Medical Expense:", df["Medical_Expense"].mean())
print(df.loc[df["Medical_Expense"].idxmax()])
print(df["Disease"].value_counts())
print(df[df["Medical_Expense"] > 50000])


# Question 15
# Create a dictionary containing information for 5 students, convert it into a DataFrame, calculate total and average marks, and display students with average above 75%.5
df = pd.read_csv("weather.csv")
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())
print("Average Temperature:", df["Temperature"].mean())
print(df[df["Temperature"] > 35])
print(df.groupby("City")["Temperature"].mean())
