#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)
print("task (1)\n")

name = input("Please enter your name : ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")  # Hello Youssef reda, Happy To See You Here.


# task (2)
print("task (2)\n")

age = int(input("Please enter your age :"))

if(age<16) :

   print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")  # Hello Your Age Is Under 16, Some Articles Is Not Suitable For You

else:
   print(f"Hello Your Age Is {age}, All Articles Is Suitable For You" )  # Hello Your Age Is 22, All Articles Is Suitable For You

# task (3)
print("task (3)\n")

firstname = input("Please enter your first name : ").strip().capitalize()
secondname = input("Please enter your name second : ").strip().capitalize()
second = secondname[0]
print(f"Hello {firstname} {second}.")  # Hello Youssef R.


# task (4)
print("task (4)\n")

email = input("Please enter your email : ").strip().lower()
name = email[:email.index("@")].capitalize()
domain = email[email.index("@") + 1 : email.index(".")]
topdomain = email[email.index(".") + 1 : ]

print(f"your name is {name}")  # your name is Joo55
print(f"your Email Service Provider Is {domain}")  # your Email Service Provider Is gmail
print(f"top Level Domain Is {topdomain}")  # top Level Domain Is com

