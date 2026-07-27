#below_average problems
#1.check_num is zero or non-zero
def zero_non_zero():
    x=int(input("Enter any number:"))
    if x==0:
        print("Given no. is a zero no.")
    else:
        print("Given no. is non-zero")
zero_non_zero()

#2.find largest of two numbers
def largest():
    x=int(input("Enter first number:"))
    y=int(input("Enter another number:"))
    if x>y:
        print(f"{x} is largest")
    else:
        print(f"{y} is largest")
largest()

#3.def pos_neg():
    o=int(input("Enter any number"))
    if o>0:
        print(f"{o} is a positive number")
    else:
        print(f"{o} is a negative number")
pos_neg()

#4.to check entered character is vowel or consonant
def vowel_consonants():
    ch = input("Enter an alphabet:")
    if len(ch) ==1  and ch.isalpha():
        if ch in "aeiouAEIOU":
            print("vowel")
        else:
            print("consonant")
    else:
        print("Invalid input")
vowel_consonants()


#average problems
# 1. Evaluate Student Performance
per = float(input("Enter Percentage: "))

if per >= 90:
    print("Excellent Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print("Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")


# 2. Largest of Three Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("Largest Number =", a)
elif b >= a and b >= c:
    print("Largest Number =", b)
else:
    print("Largest Number =", c)


# 3. Smallest of Three Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a <= b and a <= c:
    print("Smallest Number =", a)
elif b <= a and b <= c:
    print("Smallest Number =", b)
else:
    print("Smallest Number =", c)


#above average problems
# 1. Check Whether Number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 2. Check Whether a Year is Leap Year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 3. Driver Insurance Eligibility
marital = input("Enter Marital Status (married/unmarried): ")

if marital == "married":
    print("Driver is Insured")
else:
    gender = input("Enter Gender (male/female): ")
    age = int(input("Enter Age: "))

    if gender == "male" and age > 30:
        print("Driver is Insured")
    elif gender == "female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")
  
