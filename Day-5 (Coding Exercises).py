#type conversion and casting
string = "Thanooj kumar"
length = len(string)
print(length)
print(len("Thanooj kumar"))
print(10+10)
print("10"+"10")
print(10+float(10))
print(10+int(10.653232))
name = "123"
print(10+int(name))
length = len("Thanooj kumar")
print("Your name has"+" "+str(length)+" " +"Characters")
name = input("Enter your name:")
length = len(name)
print("Your name has"+" "+str(length)+" " +"Characters")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print(addition)
print(subtraction)
print(multiplication)
print(division)
number =input("Enter a two digit number:")
first_digit = int(number[0])
second_digit =int(number[1])
print(first_digit+second_digit)
#operators(arithmetic)
print(2-1)
print(2+1)
print(2*2)
print(2/2)
print(3**2)
print(3//2)
print(5%2)
print(5+4*3)
print(2**3)
print(5+2*3-1+10//5)
weight = int(input("Enter your weight:"))
height = float(input("Enter your height:"))
bmi = weight/height**2
print(bmi)
#assignment operators
a = 5
a +=2
print(a)
a/=2
print(a)
a//=2
print(a)
a = 9
a%=2
print(a)
a,b,c = 45,55,65
print(a,b,c)
a,b= 45,55
a +=5
print(a)
a,b = 4,3
c = a+b
print(c)
c +=a
print(c)
c -=a
print(c)
c *=a
print(c)
c //= a
print(c)
a,b = 10,20
c = a+b
print(c)
c +=a
print(c)
c //= b
print(c)
c%=b
print(c)
#comparison operators
a = 50
print(a ==56)
print(a <=53)
print(a >= 49)
print(a!=49)
print((a+1)!=53)
#logical operators
a,b = 10,25
c = True
print(a<=10 and c)
print(a>10 and c)
print(a<11 and c)
print(a==10 and c)
print(a!=11 and c)
print(a<11 and b==25)
print(a>11 or b==25)
print(a>=11 or c)
print(a == 10 or b >25)
print(a != 10 or c > 25)
print(a == 10 or b == 25)
#bitwise operators
a = 5
b = 4
print(a & b)
print(a | b)
print(a ^ b)
print(a<<2)
print(a>>2)
print(~a)
print(~b)
#identity operators
a = 5
b = 10
print(a is b)
print(a is not b)
print(id(a))
print(id(b))
#membership operators
str = "Thanooj"
print('j'in str)
print('k'not in str)
print('T'in str)
print("T"in str)
print('t'not in str)
print('t'in str)
weight = int(input("Enter your weight:"))
height = float(input("Enter your height:"))
bmi = weight/height**2
print(int(bmi))
#Round function
print(round(11.5))
print(round(12.5))
print(round(6.77,1))
print(round(6.77,2))
print(round(6.7790887,3))
print(round(6.77,-1))
print(round(66.77,-2))
print(round(1212,-2))
print(round(1212,-3))
print(round(467,-3))
print(round(7.6666))
print(type(round(7.6666)))
#F-strings
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
print(f"Your name is {name}. Your age is {age}. Your height is {height}.")
age = int(input("Enter your age:"))
Years_left = 100-age
months_left = 12*Years_left
weeks_left = 52*Years_left
days_left = 365*Years_left
print(f"You left {Years_left} years. You left {months_left} months. You left {weeks_left} weeks. You left {days_left} days.")
#conditional statements
#if-else
height = int(input("Enter your height:"))
if height>=3:
    print("You can ride.")
else:
    print("You can't ride.")
number = int(input("Enter a number:"))
if number % 2 !=0:
    print("Odd number")
else:
    print("Even number")
#Nested if-else
height = float(input("Enter your height:"))
if height >= 2.5:
    print("You can ride.")
    age = int(input("Enter your age:"))
    if age <= 18:
        print("Your ticket price is 250.")
    else:
        print("Your ticket price is 500.")
else:
    print("You can't ride.")
height = float(input("Enter your height:"))
if height >= 2.5:
    print("You can ride.")
    age = int(input("Enter your age:"))
    if age <= 12:
        print("Your ticket price is 125")
    elif age <=18:
        print("Your ticket price is 250.")
    else:
        print("Your ticket price is 500.")
else:
    print("You can't ride.")
number = int(input("Enter a number:"))
if number ==1:
    print("1")
elif number ==2:
    print("2")
elif number ==3:
    print("3")
elif number ==4:
    print("4")
else:
    print("wrong input")
weight = int(input("Enter your weight:"))
height = float(input("Enter your height:"))
bmi = weight/height**2
if bmi<18.5:
    print(f"Your bmi is {bmi} and You are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi} and you are normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi} and you are over weight")
elif bmi<35:
    print(f"Your bmi is {bmi} and you are obesed")
else:
    print(f"Your bmi is {bmi} and you are clinically obessed")
year = int(input("Which year you want to check:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
         print("Not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
#Multiple if statements
height = float(input("Enter your height:"))
bill = 0
if height >= 2.5:
    print("You can ride.")
    age = int(input("Enter your age:"))
    if age <=12:
        print("Your ticket price is 125")
        bill = 125
    elif age <=18:
        print("Your ticket price is 250.")
        bill = 250
    else:
        print("Your ticket price is 500.")
        bill = 500
else:
    print("You can't ride.")
want_photo= input("Do you want to take photo(Y/N):")
if want_photo=="Y" or want_photo=="y":
    bill = bill + 50
    print(f"Your total bill is {bill}")
size = input("Which pizza do you want:")
bill = 0
if size =="s" or size =="S":
    print("Your prize is 100")
    bill +=100
elif size =="m" or size =="M":
    print("Your prize is 150")
    bill +=150
else:
    print("Your prize is 200")
    bill +=200
add_pepperoni = input("Do you want to add pepperoni(Y/N):")
if add_pepperoni=="Y" or add_pepperoni=="y":
    if size =="s" or size == "S":
        bill += 30
    else:
        bill += 50
extra_cheese = input("Do you want to add extra cheese(Y/N):")
if extra_cheese=="Y" or extra_cheese=="y":
    bill +=20
print(f"Your total bill is {bill}")
name1 = input("What is your name?")
name2 = input("What is his/her name?")
combine_string = name1 + name2
lower_case_string =combine_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true =t+r+u+e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e
love_score = int(str(true) + str(love))
if love_score <10 or love_score >90:
    print(f"Your love score is {love_score} and you go together like coke and mentos.")
elif love_score >=40 and love_score <50:
    print(f"Your love score is {love_score} and you are alright together.")
else:
    print(f"Your love score is {love_score}.")
