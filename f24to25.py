#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)

name = "USF_reda",
print(name)  # ('USF_reda',)
print(type(name))  # <class 'tuple'>


# task (2)

frinds = ("osama", "joo", "mona")
changeType = list(frinds)
list(frinds) [0] = "Elzero"
print(frinds)



# task (3)

nums = (1, 2, 3)
letters = ("A", "B", "C")
add = nums + letters
print(add)  # (1, 2, 3, 'A', 'B', 'C')
print(len(add))  # 6


# task (4)

nums = letters

print(nums[0])  # A
print(nums[1])  # B
print(nums[2])  # C