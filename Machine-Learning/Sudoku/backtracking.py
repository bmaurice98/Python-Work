import sys


def permute(list, s):
    if list == 1:
        return s
    else:
        return [y + x for x in permute(list, s) for y in permute(list - 1, s)]


list1 = ["a", "b", "c"]
list2 = [1, 2, 4, 55, 6, 44, 84, 3, 9]
print(permute(1, list1))
print(permute(2, list2))
# print(sys.setrecursionlimit(3000))
