name = 'Thanooj'
age = 22
height = 1.7
print("My name is: ",name,"Iam",age,"Years old","My height is",height,"Meters")
print(f"My name is {name} and Iam {age} years old and My height is {height} mrters")
print(f"Thanooj Father's age is {age*2}")
age =int(input("Enter your age:"))
Years_left = 100 - age
Months_left = Years_left * 12
Weeks_left = Years_left * 52
Days_left = Years_left * 365
print(f"You have {Years_left} years left, {Months_left} months left, {Weeks_left} weeks left and {Days_left} days left")
days =int(input("number of days in a week:"))
total_hours = days * 24
total_minutes = total_hours * 60
total_seconds = total_minutes * 60
print(f"In a week there will be {total_hours} hours and {total_minutes} minutes and {total_seconds} seconds")
#conditional statements
number = int(input("Enter a number:"))
if number%2 ==0:
    print("The number is even")
else:
    print("The number is odd")
height = float(input("What is your height:"))
if height >= 3:
    print("You can ride")
    age = int(input("enter your age:"))
    if age<=18:
        print("Ticket price is 250")
    else:
        print("Ticket price is 500")
else:
    print("You can't ride")
print("Thank you and visit again!!")
height = float(input("Enter your height:"))
if height >=3:
    print("You can ride")
    age = int(input("enter your age:"))
    if age<12:
        print("Ticket price is 125")
    elif age<=18:
        print("Ticket price is 250")
    else:
        print("Ticket price is 500")
else:
    print("You can't ride")
print("Thank you and visit again!!")
weight = float(input("enter weight in kg:"))
height = float(input("enter height in meters:"))
bmi = weight /height**2
if bmi<18.5:
    print("You are underweight")
elif bmi<25:
    print("You are normal")
elif bmi<30:
    print("You are overweight")
elif bmi<35:
    print("You are obese")
else:
    print("You are clinically obese")
year = int(input("which year you want to check:"))
if year%4 ==0:
    if year%100 ==0:
        if year%400 ==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

height = int(input("enter your height:"))
bill= 0
if height >=3:
    print("You can ride")
    age = int(input("enter your age:"))
    if age<=12:
        bill = 125
        print("Ticket price is 125")
    elif age<=18:
        bill = 250
        print("Ticket price is 250")
    else:
        bill = 500
        print("Ticket price is 500")
else:
    print("You can't ride")
want_photo = input("Do you want a photo(Y/N)?")
if want_photo=="Y" or want_photo=="y":
    bill = bill + 50
    print(f"Your total bill is {bill}")
print("Thank you and visit again!!")
size = input("What size pizza do you want(S/M/L?")
bill = 0
if size == "s" or size =="S":
    print("Small size pizza price is 100")
    bill = 100
elif size == "m" or size =="M":
    print("Medium size pizza price is 200")
    bill = 200
else:
    print("Large size pizza price is 300")
    bill = 300
add_pepperoni = input("Do you want to add pepperoni?(Y/N)?")
if add_pepperoni == "Y" or add_pepperoni =="y":
    if size =="s" or size =="S":
        bill+=30
    else:
        bill+=50
extra_cheese =input("Do you want to add extra cheese?(Y/N)?")
if extra_cheese == "Y" or extra_cheese =="y":
    bill+=20
print(f"Your total bill is {bill}")
name1 =input("What is your name?")
name2 =input("what is his/her name?")
combine_string = name1 + name2
lower_case_string = combine_string.lower()
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t+r+u+e
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l+o+v+e
love_score = int(str(true)+str(love))
if love_score <10 or love_score >90:
    print(f"Your love score is {love_score} and you are together like cola and mentos")
elif love_score >=40 and love_score <= 50:
    print(f"your love score is {love_score} and you are alright together")
else:
    print(f"your love score is {love_score}")
age = int(input("Enter your age:"))
if age >=18:
    print("You are eligible for vote")
else:
    print("You are not eligible  for vote")
