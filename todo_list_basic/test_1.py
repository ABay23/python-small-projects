filenames = ["New.York.txt", "New.Jersey.txt"]

# filename = filenames[0]

# filename_2 = filename.replace('.', '-', 1)

# filenames[0] = filenames[0].replace('.', '-', 1)

for city in filenames:
    city = city.replace('.', '-', 1)
    print(city)

# print(filename)
# print(filename_2)
print(filenames)
