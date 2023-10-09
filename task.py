# 1
# a = int(input()); b = int(input())
# for i in range(a, b + 1):
#     print(i)

# 2
# a = int(input()); b = int(input()); l = []
# for i in range(min(a, b), max(a, b) + 1):
#          l.append(i)
# l.sort()
# if a > b:
#     l.reverse()
# else:
#     pass
# print(l)

# a = int(input()); sm = 0
# for i in range(a):
#     num = int(input())
#     sm += num
# print(sm)

# n = int(input()); s = 1
# for i in range(1, n+1):
#     s *= i
# print(s)

# n = int(input())
# for i in range(n):
#     for j in range(1, i + 2):
#         print(j, end='')
#     print()

# n =int(input()); l = []
# for i in range(1, n):
#     if i ** 2 < n:
#         l.append(i**2)
# print(l)

# n = int(input())
# x = 2
# p = 1
# while x <= n:
#     x *= 2
#     p += 1
# print(p - 1, x // 2)

# x = int(input()); y = int(input()); z = 1
# while x < y:
#     d = x / 100 * 10
#     x += d
#     z += 1
# print(z)

# l = 0
# while int(input()) != 0:
#     l += 1
# print(len)

# x = int(input())
# a = 0
# while x != 0:
#     n = int(input())
#     if n != 0 and x < n:
#         a += 1
#     x = n
# print(a)

# n = int(input())
# if n == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     print(b)

# p = -1
# c = 0
# m = 0
# e = int(input())
# while e != 0:
#     if p == e:
#         c += 1
#     else:
#         p = e
#         m = max(m, c)
#         c = 1
#     e = int(input())
# m = max(m, c)
# print(m)

# a = input().split()
# for i in range(0, len(a), 2):
#     print(a[i])

# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

# index = 0
# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[index]:
#         index = i
# print(a[index], index)

# a = [int(i) for i in input().split()]
# x = int(input())
# p = 0
# while p < len(a) and a[p] >= x:
#     p += 1
# print(p + 1)

# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))

# a = [int(s) for s in input().split()]
# indexmi = 0
# indexma = 0
# for i in range(1, len(a)):
#     if a[i] > a[indexma]:
#         indexma = i
#     if a[i] < a[indexmi]:
#         indexmi = i
# a[indexmi], a[indexma] = a[indexma], a[indexmi]
# print(' '.join([str(i) for i in a]))

# a = [int(s) for s in input().split()]
# k = int(input())
# for i in range(k + 1, len(a)):
#     a[i - 1] = a[i]
# a.pop()
# print(' '.join([str(i) for i in a]))

# a = [int(s) for s in input().split()]
# k, C = [int(s) for s in input().split()]
# a.append(0)
# for i in range(len(a) - 1, k, -1):
#     a[i] = a[i - 1]
# a[k] = C
# print(' '.join([str(i) for i in a]))

# n = 8
# x = []
# y = []
# for i in range(n):
#     new_x, new_y = [int(s) for s in input().split()]
#     x.append(new_x)
#     y.append(new_y)
# c = True
# for i in range(n):
#     for j in range(i + 1, n):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             c = False
# if c:
#     print('NO')
# else:
#     print('YES')