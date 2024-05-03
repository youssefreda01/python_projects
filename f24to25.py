#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)
print("task (1)\n")

name = "USF_reda",
print(name)  # ('USF_reda',)
print(type(name))  # <class 'tuple'>


# task (2)
print("task (2)\n")

frinds = ("osama", "joo", "mona")
changeType = list(frinds)
changeType [0] = "Elzero"
frinds = changeType
print(frinds)          #  ['Elzero', 'joo', 'mona']
changeType2 = tuple(frinds)
frinds = changeType2
print(type(frinds))    #  <class 'tuple'>

print(len(frinds))  # 3


# task (3)
print("task (3)\n")

nums = (1, 2, 3)
letters = ("A", "B", "C")
add = nums + letters
print(add)  # (1, 2, 3, 'A', 'B', 'C')
print(len(add))  # 6


# task (4)                     # Destruct
print("task (4)\n")

nums = letters

print(nums[0])  # A
print(nums[1])  # B
print(nums[2])  # C
