import random


def generate(n):
    m = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            m[i][j] = random.randint(0, 1)
            m[j][i] = m[i][j]
    return m


def print_matrix(m, names):
    print("    ", end="")
    for s in names:
        print(s.ljust(4), end="")
    print()
    for i in range(len(m)):
        print(names[i].ljust(4), end="")
        for j in range(len(m)):
            print(str(m[i][j]).ljust(4), end="")
        print()


def expand(m, n):
    a = [[0] * n for i in range(n)]
    for i in range(len(m)):
        for j in range(len(m)):
            a[i][j] = m[i][j]
    return a


n1 = int(input("Enter number of vertices of G1 (2..10): "))
n2 = int(input("Enter number of vertices of G2 (2..10): "))
if n1 < 2 or n1 > 10 or n2 < 2 or n2 > 10:
    print("Invalid input.")
    exit()

print("\n Task 3 ")
m1 = generate(n1)
m2 = generate(n2)

n = max(n1, n2)
k = min(n1, n2)
names = []
for i in range(n):
    names.append("v" + str(i + 1))

print("G1 adjacency matrix:")
print_matrix(m1, names[:n1])
print("G2 adjacency matrix:")
print_matrix(m2, names[:n2])

a = expand(m1, n)
b = expand(m2, n)

res = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        res[i][j] = a[i][j] | b[i][j]
print("a) Union G1 U G2:")
print_matrix(res, names)

res = [[0] * k for i in range(k)]
for i in range(k):
    for j in range(k):
        res[i][j] = m1[i][j] & m2[i][j]
print("b) Intersection G1 & G2:")
print_matrix(res, names[:k])

tmp = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        tmp[i][j] = a[i][j] ^ b[i][j]

keep = []
for i in range(n):
    if sum(tmp[i]) > 0:
        keep.append(i)

res = [[0] * len(keep) for i in range(len(keep))]
ring_names = []
for i in range(len(keep)):
    ring_names.append(names[keep[i]])
    for j in range(len(keep)):
        res[i][j] = tmp[keep[i]][keep[j]]

print("c) Ring sum G1 (+) G2:")
if len(keep) == 0:
    print("Empty graph")
else:
    print_matrix(res, ring_names)
