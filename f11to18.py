#------------------------------
# this code made by USF_reda
# thank you eng.momen
#------------------------------

# task (1)

name = "USF_reda"
age = "18"
country = "Egypt"

print(f"\"Hello '{name}', How You Doing \\ \"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")  

 # "Hello 'USF_reda', How You Doing \ "" Your Age Is "18"" + And Your Country Is: Egypt


# task (2)

print(f"\"Hello '{name}', How You Doing \\\n \"\" Your Age Is \"{age}\"\" +\n And Your Country Is: {country}")  

# "Hello 'USF_reda', How You Doing \
#  "" Your Age Is "18"" +
# And Your Country Is: Egypt


# task (3)

name2 = "Zeus_code"
print(name2[1])  # e
print(name2[2])  # u
print(name2[-1])  # e


# task (4)

print(name2[1:4])  # eus_
print(name2[0::2])  # Zu_oe
print(name2[::-2])  # e


# task (5)

name3 = "#@#@Zeus#@#@"
print(name3.strip("#@#@"))  # Zeus

# task (6)

num0 = "7"
num1 = "18"
num2 = "199"
num3 = "1666"

print(num0.zfill(4))  # 0007
print(num1.zfill(4))  # 0018
print(num2.zfill(4))  # 0199
print(num3.zfill(4))  # 1666


# task (7)

print(name.rjust(20,"@")) # @@@@@@@@@@@@USF_reda
print(name2.rjust(20,"@"))  #  @@@@@@@@@@@Zeus_code


# task (8)

n1 = "PPPbbb"
n2 = "BBBppp"
print(n1.swapcase())  # pppBBB
print(n2.swapcase())  # bbbPPP

# task (9)

msg = "i love you i love you i love you"
print(msg.count("love"))  # 3


# task (10)

print(name2.index("c"))  # 5


# task (11)

msg2 = "i <3 python and i <3 elzero web school" 
print(msg2.replace("<3", "love", 1))  # i love python and i <3 elzero web school

# task (12)

msg2 = "i <3 python and i <3 elzero web school" 
print(msg2.replace("<3", "love"))  # i love python and i love elzero web school


# task (13)

name = "USF_reda"
age = 18
country = "Egypt"

print(f"name = {name} \nage = {age} \ncountry = {country}")

#name = USF_reda
#age = 18
#country = Egypt
