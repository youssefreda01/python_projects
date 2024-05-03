
#------------------------------
# this code made by USF_reda
#------------------------------

# task (1)
print("task (1)\n")

myfrinds =["moaz", "fares", "mohamed", "ali", "osama"]

print(myfrinds[0])  #moaz
print(myfrinds[-5]) #moaz
print(myfrinds[4]) #osama
print(myfrinds[-1]) #osama


# task (2)
print("task (2)\n")

print(myfrinds[0::2])  # ['moaz', 'mohamed', 'osama']
print(myfrinds[1::2])  # ['fares', 'ali']


# task (3)
print("task (3)\n")

print(myfrinds[1:4]) # ['fares', 'mohamed', 'ali']
print(myfrinds[3:5]) # ['ali', 'osama']


# task (4)
print("task (4)\n")

myfrinds[3:4] = ["Zeus", "Zeus"]
print(myfrinds[0:5]) # ['moaz', 'fares', 'mohamed', 'Zeus', 'Zeus']


# task (5)
print("task (5)\n")

myfrinds.insert(0, "beshoy")
myfrinds.append("marim")

print(myfrinds)  # ['beshoy', 'moaz', 'fares', 'mohamed', 'Zeus', 'Zeus', 'osama', 'marim']


#  task (6)
print("task (6)\n")

myfrinds.remove("beshoy")
myfrinds.remove("moaz")
print(myfrinds)  # ['fares', 'mohamed', 'Zeus', 'Zeus', 'osama', 'marim']

myfrinds.remove("marim")
print(myfrinds)  # ['fares', 'mohamed', 'Zeus', 'Zeus', 'osama']

#  task (7)
print("task (7)\n")

print("============================================================")
frinds0 = ["logy", "adel"]
frinds1 = ["joo", "adm"]
frinds2 = ["ezz", "rahma"]

frinds0.extend(frinds1)
frinds0.extend(frinds2)
print(frinds0) # ['logy', 'adel', 'joo', 'adm', 'ezz', 'rahma']


#  task (8)
print("task (8)\n")

frinds0.sort()
print(frinds0) # ['adel', 'adm', 'ezz', 'joo', 'logy', 'rahma']

frinds0.sort(reverse=True)
print(frinds0)  # ['rahma', 'logy', 'joo', 'ezz', 'adm', 'adel']


#  task (9)
print("task (9)\n")

print(len(frinds0))  # 6


#  task (10)
print("task (10)\n")

languages = ["c++", "html", "JS", "python"]
other =["web", "cyber", "flutter"]

languages.append(other)
print(languages)  # ['c++', 'html', 'JS', 'python', ['web', 'cyber', 'flutter']]

print(languages[4][0]) # web
print(languages[4][-1]) # flutter



