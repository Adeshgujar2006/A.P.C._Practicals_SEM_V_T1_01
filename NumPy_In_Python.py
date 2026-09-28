#1.Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.
import numpy as np
# arr=np.array([10,20,30,40,50,60,70,80,90,100])
# print(arr)
# print("Size:",arr.size)
# print("Datatype:",arr.dtype)
# print("Number of dimensions:",arr.ndim)

#2.Create 2 numpy arrays of 5 integers each.Perform and display:Addition,Subtraction,Multiplication,Division,Modulus
# arr1=np.array([2,3,5,6,7,8,9])
# arr2=np.array([11,13,15,16,17,18,19])
# print("Addition:",arr1+arr2)
# print("Multiplication:",arr1*arr2)
# print("Subtraction:",arr1-arr2)
# print("Division:",arr1/arr2)
# print("Modulus:",arr1%arr2)

#3.	Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.
# arr=np.array([10,15,20,30,25,45,60,70,85,71])
# print("Maximum of the array:",np.max(arr))
# print("Minimum of the array:",np.min(arr))
# print("Sum of all elements of the array:",np.sum(arr))
# print("Average of all elements of the array:",np.mean(arr))

#4.	Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# print("Even no.s in integers from 1 to 20",arr[arr%2==0])
# print("Odd no.s in integers from 1 to 20",arr[arr%2!=0])

#5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
# •	2 × 6 matrix 
# •	3 × 4 matrix 
# •	4 × 3 matrix

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("Required 2 x 6 matrix:\n",arr.reshape(2,6))
# print("Required 3 X 4 matrix:\n",arr.reshape(3,4))
# print("Required 4 X 3 matrix:\n",arr.reshape(4,3))

#6.	Create two 3 × 3 NumPy matrices and perform matrix addition.
# arr1=np.array([[2 ,3, 6],
#                [5 ,4 ,8],
#                [2, 6, 3]])
# arr2=np.array([[2, 8, 9],
#                [8, 9, 7],
#                [4, 5, 9]])
# print("Addition of the two matrices is:\n", arr1+arr2)

#7.	Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
# arr1=np.array([[4, 5, 6],
#                [1, 2, 3],
#                [7, 8, 9]])
# arr2=np.array([[4,7, 1 ],
#                [5, 6, 9],
#                [12, 4, 10]])
# print(np.matmul(arr1,arr2))

#8.	Create a 3 × 4 matrix and display its transpose
# arr=np.array([[1, 2, 4, 8],
#      [4, 8, 9, 6],
#      [8, 5, 2, 3]])
# print("Transpose of the 3 X 4 array of the matrix created is:\n",arr.T)

#9.	Create a 4 × 4 NumPy array and write a program to:
# •	Display the first row 
# •	Display the last column 
# •	Display the diagonal elements 
# •	Display the elements from the second and third rows

# arr=np.array([[1, 4, 7],
#               [2, 5, 8],
#               [3, 6, 9]])

# print("First row of the array is:\n",arr[0])
# print("Last column of the array is:\n",arr[:,-1])
# print("Diagonal Elements of the array is:\n",np.diag(arr))
# print("Elements from the second and third rows:\n",arr[1:3])

#10.Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
# arr=np.array([[2, 5, 8, 1],
#               [1, 5, 9, 14],
#               [11, 12, 16, 18],
#               [7, 6, 8, 22]])

# print("Sum of the elements in each row:",np.sum(arr, axis=1))
# print("Sum of the elements in each column:",np.sum(arr, axis=0))

#11.	Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Alternate elements 
# •	Elements in reverse order
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# print("First 5 elements of the array:",arr[:5])
# print("Last 5 elements of the array:",arr[-5:])
# print("Alternate elements of the array:",arr[::2])
# print("Elements in reverse order are:",arr[::-1])

# 12. Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
# arr = np.array([10, 25, 51, 60, 35, 75, 40, 90, 45, 100])
# arr[arr > 50] = 0
# print(arr)



# 13. Create an unsorted NumPy array and display it in:
# Ascending order
# Descending order

# arr = np.array([45, 12, 78, 3, 56, 23, 89, 34])

# print("Ascending order:", np.sort(arr))
# print("Descending order:", np.sort(arr)[::-1])



# 14. Create an array containing duplicate values. Find and display only the unique elements.
# arr = np.array([1, 2, 3, 2, 4, 5, 1, 6, 3, 7])
# print("Unique elements:", np.unique(arr))



# 15. Create two NumPy arrays and concatenate them horizontally and vertically.

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print("Horizontal:", np.hstack((a, b)))
# print("Vertical:\n", np.vstack((a, b)))



# 16. Store marks of 10 students in a NumPy array. Calculate:
# Highest marks
# Lowest marks
# Average marks
# Median
# Standard deviation

# marks = np.array([78, 85, 92, 67, 88, 76, 95, 82, 73, 90])
# print("Highest marks:", np.max(marks))
# print("Lowest marks:", np.min(marks))
# print("Average marks:", np.mean(marks))
# print("Median:", np.median(marks))
# print("Standard deviation:", np.std(marks))



# 17. Take marks of 20 students, calculate the class average and display the marks of students
# who scored above the average.

# marks = np.array([65, 78, 82, 90, 55, 72, 88, 95, 61, 84,
#                   76, 69, 91, 58, 73, 87, 80, 66, 92, 75])
# average = np.mean(marks)
# print("Class average:", average)
# print("Marks above average:", marks[marks > average])



# 18. Write a Python program using NumPy to create a 3D array of shape (2, 3, 4) containing
# numbers from 1 to 24. Display the array and its:
# Number of dimensions
# Shape
# Size

# arr = np.arange(1, 25).reshape(2, 3, 4)
# print(arr)
# print("Number of dimensions:", arr.ndim)
# print("Shape:", arr.shape)
# print("Size:", arr.size)



# 19. Create a 3D array of shape (2, 3, 4) and write a program to access:
# First element
# Last element
# Element at index [0,1,2]
# Element at index [1,2,3]

# arr = np.arange(1, 25).reshape(2, 3, 4)
# print("First element:", arr[0, 0, 0])
# print("Last element:", arr[-1, -1, -1])
# print("Element at [0,1,2]:", arr[0, 1, 2])
# print("Element at [1,2,3]:", arr[1, 2, 3])



# 20. Create a (2, 3, 4) array and calculate:
# Sum of all elements
# Sum of each layer
# Sum along rows
# Sum along columns

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("Sum of all elements:", np.sum(arr))
# print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
# print("Sum along rows:", np.sum(arr, axis=2))
# print("Sum along columns:", np.sum(arr, axis=1))



# 21. Create a 3D array of random integers between 1 and 100. Replace all values greater than
# 50 with 0.

# arr = np.random.randint(1, 101, size=(2, 3, 4))

# arr[arr > 50] = 0

# print(arr)



# 22. Generate a random 3D array of shape (3, 4, 5) and calculate its:mean, median, standard deviation, variance, minimum, and maximum.
# arr = np.random.randint(1, 101, size=(3, 4, 5))
# print("Mean:", np.mean(arr))
# print("Median:", np.median(arr))
# print("Standard deviation:", np.std(arr))
# print("Variance:", np.var(arr))
# print("Minimum:", np.min(arr))
# print("Maximum:", np.max(arr))

#23.Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24. Flatten the array into a one-dimensional array and display both the original and flattened arrays.
# arr=np.arange(1,25).reshape(2,3,4)
# flat=arr.flatten()
# print("Original array:\n",arr)
# print("Array after flattened:\n",flat)

#24.Create a 3D array containing integers from 1 to 27. Flatten the array and calculate:
# •	Sum 
# •	Average 
# •	Maximum 
# •	Minimum

# arr=np.arange(1,28).reshape(3,3,3)
# flat=arr.flatten()
# print("3D Array initially:\n",arr)
# print("Array after flattened:\n",flat)
# print("Sum of flattened array:\n",np.sum(flat))
# print("Average of flattened array:\n",np.mean(flat))
# print("Maximum of flattened array:\n",np.max(flat))
# print("Minimum of fllattened array:\n",np.min(flat))

#25.Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are:
# •	Greater than 50 
# •	Even numbers 
# •	Less than the average value

# arr=np.random.randint(1, 101, size=(3, 4, 5))
# flat=arr.flatten()
# average=np.mean(flat)
# print("Original array:\n",arr)
# print("Greater than 50:\n", flat[flat > 50])
# print("Even numbers:\n", flat[flat % 2 == 0])
# print("Less than average:\n", flat[flat < average])
