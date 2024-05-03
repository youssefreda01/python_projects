#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)
print("task (1)\n")

print(100>20)  # True
print(100<200)  # True
print(100==100)  # True
print(not 100==1000)  # True

print(100<=10)  # False
print(100<=10 and 80 > 20)  # False
print(100<=10 or 80 > 901)  # False
print(500==499)  # False


# task (2)
print("task (2)\n")

html = 90
css = 70
Java = 50

print(html and css and Java > 50)  # False


# task (3)
print("task (3)\n")

num1 = 10
num2 = 20
num = 20

print(num>num1 or num>num2)  # True
print(num>num1 and num>num2)  # False


# task (4)
print("task (4)\n")

num1 = 10
num2 = 20
result = num1 + num2

print(result)  # 30
result**= 3
print(result)  # 27000
result%=26000
print(result)  # 1000
result/=5
print(result)  # 200.0
print(type(str(result)))  # <class 'str'>