import random


def generate(n):
    m = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            m[i][j] = random.randint(0, 1)
            m[j][i] = m[i][j]
    return m


def print_matrix(m, names, w):
    print(" " * w, end="")
    for s in names:
        print(s.ljust(w), end="")
    print()
    for i in range(len(m)):
        print(names[i].ljust(w), end="")
        for j in range(len(m)):
            print(str(m[i][j]).ljust(w), end="")
        print()


n1 = int(input("Enter number of vertices of G1 (2..10): "))
n2 = int(input("Enter number of vertices of G2 (2..10): "))
if n1 < 2 or n1 > 10 or n2 < 2 or n2 > 10:
    print("Invalid input.")
    exit()

print("\n=== Task 4* ===")
m1 = generate(n1)
m2 = generate(n2)

names1 = []
for i in range(n1):
    names1.append("v" + str(i + 1))
names2 = []
for i in range(n2):
    names2.append("v" + str(i + 1))
print("G1 adjacency matrix:")
print_matrix(m1, names1, 4)
print("G2 adjacency matrix:")
print_matrix(m2, names2, 4)

n = n1 * n2
names = []
for i in range(n1):
    for a in range(n2):
        names.append("(" + str(i + 1) + "," + str(a + 1) + ")")

res = [[0] * n for i in range(n)]
for i in range(n1):
    for a in range(n2):
        for j in range(n1):
            for b in range(n2):
                if (i == j and m2[a][b] == 1) or (a == b and m1[i][j] == 1):
                    res[i * n2 + a][j * n2 + b] = 1

print("Cartesian product G1 x G2:")
print_matrix(res, names, 8)
