# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
#
# print(x, y, z)


# dd = { "1":"0", "0":"1"}
# for x in dd.vals():
#     print(x, end="")


# lst = [[x for x in range(3)] for y in range(3)]
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")


# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
#
# print(fun(fun(2)))


# nums = [1, 2, 3]
# vals = nums
# print(vals)
# del vars[:]
# print(vals)


# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)


# tup = (1,2,4,8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup) ## 4

# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)


# def fun(x,y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)
# print(fun(0, 3))


# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)


# dot = {'one':'two', 'three':'one', 'two':'three'}
# v = dot['three']
# for k in range(len(dot)):
#     v = dot[v]
# print(v)


# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")


# list = [x * x for x in range(5)]
# def fun(lst):
#     del lst[lst[2]]
#     return lst
# print(fun(list))


# print("a", "b", "c", sep="sep")


# def fun(inp=2, out=3):
#     return inp * out
# print(fun(out=2))


# nums = [1,2,3]
# vals = nums


# lst = [i for i in range(-1, -2)]
# print(lst)


# def func(a, b):
#     return b ** a
# print(func(b = 2, 2))


# def func1(a):
#     return None
# def func2(a):
#     return func1(a) * func1(a)
# print(func2(2))


# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
# for x in dct.keys():
#     print(dct[x][1], end="")
