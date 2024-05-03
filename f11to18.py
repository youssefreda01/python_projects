#------------------------------
# this code made by USF_reda
# thank you eng.momen
#------------------------------

# task (1)
print("task (1)\n")

name = "USF_reda"
age = "18"
country = "Egypt"

print(f"\"Hello '{name}', How You Doing \\ \"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")  

 # "Hello 'USF_reda', How You Doing \ "" Your Age Is "18"" + And Your Country Is: Egypt


# task (2)
print("task (2)\n")

print(f"\"Hello '{name}', How You Doing \\\n \"\" Your Age Is \"{age}\"\" +\n And Your Country Is: {country}")  

# "Hello 'USF_reda', How You Doing \
#  "" Your Age Is "18"" +
# And Your Country Is: Egypt


# task (3)
print("task (3)\n")

name2 = "Zeus_code"
print(name2[1])  # e
print(name2[2])  # u
print(name2[-1])  # e


# task (4)
print("task (4)\n")

print(name2[1:4])  # eus_
print(name2[0::2])  # Zu_oe
print(name2[::-2])  # e


# task (5)
print("task (5)\n")

name3 = "#@#@Zeus#@#@"
print(name3.strip("#@#@"))  # Zeus

# task (6)
print("task (6)\n")

num0 = "7"
num1 = "18"
num2 = "199"
num3 = "1666"

print(num0.zfill(4))  # 0007
print(num1.zfill(4))  # 0018
print(num2.zfill(4))  # 0199
print(num3.zfill(4))  # 1666


# task (7)
print("task (7)\n")


print(name.rjust(20,"@")) # @@@@@@@@@@@@USF_reda
print(name2.rjust(20,"@"))  #  @@@@@@@@@@@Zeus_code


# task (8)
print("task (8)\n")

n1 = "PPPbbb"
n2 = "BBBppp"
print(n1.swapcase())  # pppBBB
print(n2.swapcase())  # bbbPPP

# task (9)
print("task (9)\n")

msg = "i love you i love you i love you"
print(msg.count("love"))  # 3


# task (10)
print("task (10)\n")

print(name2.index("c"))  # 5


# task (11)
print("task (11)\n")

msg2 = "i <3 python and i <3 elzero web school" 
print(msg2.replace("<3", "love", 1))  # i love python and i <3 elzero web school

# task (12)
print("task (12)\n")

msg2 = "i <3 python and i <3 elzero web school" 
print(msg2.replace("<3", "love"))  # i love python and i love elzero web school


# task (13)
print("task (13)\n")

name = "USF_reda"
age = 18
country = "Egypt"

print(f"name = {name} \nage = {age} \ncountry = {country}")

#name = USF_reda
#age = 18
#country = Egypt
