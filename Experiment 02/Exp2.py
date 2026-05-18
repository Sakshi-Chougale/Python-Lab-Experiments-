# Program to check even/odd and grade

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100 :
    print("Grade A")
elif marks >= 80 and marks <= 90:
    print("Grade B")
elif marks >= 70 and marks <= 80:
    print("Grade C")
else:
    print("Grade D")