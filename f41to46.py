#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)
print("task (1)\n")

num1 = int(input("Plaese enter number1 : "))
num2 = int(input("Plaese enter number2 : "))
operator = input("Plaese enter the operator : ").strip()

if operator == "+" : 
   
   output1 = num1 + num2
   print(f"The equation = {output1}")

elif operator == "-" :
   
   output2 = num1 - num2
   print(f"The equation = {output2}")

elif operator == "*" :
   
   output3 = num1 * num2
   print(f"The equation = {output3}")

elif operator == "/" :
   
   output4 = num1 / num2
   print(f"The equation = {output4}")

elif operator == "%" :
   
   output5 = num1 % num2
   print(f"The equation = {output5}")

else :

    print("your operator is not valid")   




# task (2)
print("task (2)\n")

age = 17

print("App Is Suitable For You" if age > 18 else "App Is Not Suitable For You")  # App Is Not Suitable For You




# task (3)
print("task (3)\n")

Age = int(input("Please enter your age : "))

if Age > 10 and Age < 100 :
   
   months = Age * 12
   weeks = months * 4
   days = weeks * 7
   houers = days * 24
   minutes = houers * 60
   seconds = minutes * 60

   print(f"your age in months = {months:,}") 
   print(f"your age in weeks = {weeks:,}") 
   print(f"your age in days = {days:,}") 
   print(f"your age in houers = {houers:,}") 
   print(f"your age in minutes = {minutes:,}") 
   print(f"your age in seconds = {seconds:,}")


else :

   print("your age is not valid") 




# task (4)
print("task (4)\n")

country = input("Input Your Country : ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 100
discount = 30

if country in countries : 
   
   print(f"Because you are from {country} the price will be {discount}")

else :
   
   print(f"There is no discount and the prise is {price}")