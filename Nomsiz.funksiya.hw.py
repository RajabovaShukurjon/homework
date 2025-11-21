# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
#
# fname = input("Ismni kiriting: ")
# lname = input("Familiyangizni kiriting: ")
# age = input("Yoshingizni kiriting: ")
#
# user_data(fname, lname, age)



# def find_max(a, b, c):
#     max_son = max(a, b, c)
#     print("Eng katta son =", max_son)
#
# a = int(input("A ni kiriting: "))
# b = int(input("B ni kiriting: "))
# c = int(input("C ni kiriting: "))
#
# find_max(a, b, c)


# def find_letter_count(word, letter):
#     count = word.lower().count(letter.lower())
#     print(f'"{word}" so‘zida "{letter}" dan {count} ta.')
#
# word = input("So‘z kiriting: ")
# letter = input("Qaysi harfni sanaymiz: ")
#
# find_letter_count(word, letter)


# def list_sum(myList):
#     print("Listning elementlar yig‘indisi =", sum(myList))
#
# myList = [10, 44, 55, 66]
# list_sum(myList)


# def daraja(a, b):
#     print(a ** b)
#
# a = int(input("A: "))
# b = int(input("B: "))
# daraja(a, b)


# def daraja4(a, b, c, d):
#     print(a ** b)
#     print(a ** c)
#     print(a ** d)
#
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
# d = int(input("D: "))
#
# daraja4(a, b, c, d)


# 7



# def add_right(a, b):
#     print(int(str(a) + str(b)))
#
# a = input("A: ")
# b = input("B: ")
#
# add_right(a, b)


# def add_left(a, b):
#     print(int(str(b) + str(a)))
#
# a = input("A: ")
# b = input("B: ")

# add_left(a, b)


# 10
# def work_with_list(a):
#     mn = min(a)
#     new_list =
#     print(new_list)
#
# a = [5, 3, 7, 2]
# work_with_list(a)



# 11
# def big_sales(sales):
#     return max(sales, key=sales.get)
#
# sales = {
#     "yanvar": 912000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 90000,
#     "dekabr": 10000
# }
#
# print("Eng katta sotuv bo‘lgan oy:", big_sales(sales))



# 12
# def min_max(numbers, max_num, min_num):
#     print("max_num to‘g‘ri:", max_num == max(numbers))
#     print("min_num to‘g‘ri:", min_num == min(numbers))
#
# nums = [3, 8, 1, 9, 4]
# min_max(nums, 9, 8)



# 13
def expensiveProduct(products):
    most_expensive = max(products, key=lambda x: x["price"])
    print("Eng qimmat telefon:", most_expensive["name"])

products = [
    {"name": "Iphone X", "price": 600},
    {"name": "Iphone 12", "price": 1500},
    {"name": "Samsung Note 9", "price": 800},
    {"name": "Samsung S10", "price": 1100},
]

expensiveProduct(products)
