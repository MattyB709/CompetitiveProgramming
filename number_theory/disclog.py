# list = []
# for i in range(2, 15):
#     ugh = False
#     for j in range(i):
#         for k in range(i):
#             if ((j**5 + k**5) % i) == ((j + k + 6) % i):
#                 ugh = True
#                 break
#         if ugh:
#             break
#     if not ugh:
#         list.append(i)
# print(list)

# # for num in list:
mod = 5
for j in range(mod):
    # for k in range(5):
        print("x ", (j**5 - j) % mod )
        print("y ", (-j**5 +  j + 6) % mod)
# for i in range(9):
#     print(i, (i**3) % 9)