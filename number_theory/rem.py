for i in range(10**7):
    if (i**5 -2 * i**4  + 2*i + 1) % 10**7 == 0:
        print(i)
# set1 = set()
# for i in range(31):
#     set1.add(i**3 % 31)
# print(set1)
# set2 = set()
# for i in range(31):
#     if i**5 % 31 == 6:
#         print(i)
#     set2.add(i**5 % 31)
# print(set2)
# set3 = set()
# for num in set1:
#     for num2 in set2:
#         if (num + num2 % 31 == 7):
#             print(num, num2)
#         set3.add((num+num2) %31)
# print(set3)
# # print (7**13 % 31)