my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
my_list3 = [1, 45, 54, 23, 67, 78, 46]

# print(my_list[3])
# print(my_list.append('baba'))
# print(my_list.append('mama'))
# print(len(my_list))
# print(my_list.insert(1, 'TUNDE'))
# print(my_list)

# if "energy" in my_list:
#     print("It is present")
# else:
#     print("NO")


# my_list.extend(my_list2)
# print(my_list)
my_list.append(my_list2)
print(my_list)
# my_list.remove("TUNDE")
# # print(my_list)
# my_list.pop(4)
# # print(my_list)

my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
my_list.reverse()
# print(my_list)
my_list.sort(reverse=True)
# print(my_list)
my_list.sort(key=str.lower)
# print(my_list)

# print(max(my_list3))
# print(min(my_list3))