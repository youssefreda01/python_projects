#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)

my_list = [1, 2, 3, 3, 4, 5, 1]
uniq_list = [1, 2, 3, 4, 5]

print(uniq_list)  # [1, 2, 3, 4, 5]
print(type(uniq_list))  # <class 'list'>
print(uniq_list[:4])  # [1, 2, 3, 4]


# task (2)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)  # {1, 2, 3, 'C', 'B', 'A'}
print(nums.union(letters))  # {1, 2, 3, 'C', 'B', 'A'}
num3 = set(nums)
num3.update(letters)
print(num3)  # {1, 2, 3, 'C', 'B', 'A'}



# task (3)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)  # {1, 2, 3}
print(my_set.clear())  # None
my_set.add("A")
my_set.add("B")
print(my_set)  # {'B', 'A'}
my_set.discard
print(my_set)  # {'B', 'A'}


# task (4)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))  # True



# task (5)

skills_dict = {
    "HTML": 90,
    "CSS": 80,
    "Python": 30
}
print(f'"HTML Progress Is {skills_dict["HTML"]}%"')  # "HTML Progress Is 90%"
print(f'"CSS Progress Is {skills_dict["CSS"]}%"')  # "CSS Progress Is 80%"
print(f'"Python Progress Is {skills_dict["Python"]}%"')  # "Python Progress Is 30%"

skills_dict ["AI"] = 60
print(f'"AI Progress Is {skills_dict["AI"]}%"')