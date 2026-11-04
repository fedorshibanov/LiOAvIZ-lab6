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


def build_lists(m):
    adj = {}
    for i in range(len(m)):
        v = "v" + str(i + 1)
        adj[v] = []
        for j in range(len(m)):
            if m[i][j] == 1:
                adj[v].append("v" + str(j + 1))
    return adj


def print_lists(adj):
    for v in adj:
        print(v.ljust(4) + ":", end=" ")
        for w in adj[v]:
            print(w, "->", end=" ")
        print("NULL")


def read_vertex(s, n):
    x = int(s)
    if x < 1 or x > n:
        print("Invalid input.")
        exit()
    return "v" + str(x)


def identify(adj, u, v):
    loop = u in adj[u] or v in adj[v] or v in adj[u]

    z = []
    for w in adj[u]:
        if w != u and w != v and w not in z:
            z.append(w)
    for w in adj[v]:
        if w != u and w != v and w not in z:
            z.append(w)

    for w in z:
        if u in adj[w]:
            adj[w].remove(u)
        if v in adj[w]:
            adj[w].remove(v)
        adj[w].append("z")

    if loop:
        z.append("z")

    del adj[u]
    del adj[v]
    adj["z"] = z


def contract(adj, u, v):
    adj[u].remove(v)
    adj[v].remove(u)
    identify(adj, u, v)


def split(adj, v):
    z = []
    for w in adj[v]:
        if w == v:
            z.append("z")
        else:
            z.append(w)
            adj[w].append("z")
    z.append(v)
    adj[v].append("z")
    adj["z"] = z


n = int(input("Enter number of vertices of G1 (2..10): "))
if n < 2 or n > 10:
    print("Invalid input.")
    exit()

print("\n=== Task 2.2* ===")
m1 = generate(n)
names = []
for i in range(n):
    names.append("v" + str(i + 1))
print("G1 adjacency matrix:")
print_matrix(m1, names)
print("G1 adjacency lists:")
print_lists(build_lists(m1))

s = input("a) Identification of vertices. Enter u and v: ").split()
u = read_vertex(s[0], n)
v = read_vertex(s[1], n)
if u == v:
    print("Invalid input.")
    exit()
adj = build_lists(m1)
identify(adj, u, v)
print_lists(adj)

s = input("b) Contraction of an edge. Enter u and v: ").split()
u = read_vertex(s[0], n)
v = read_vertex(s[1], n)
if u == v:
    print("Invalid input.")
    exit()
adj = build_lists(m1)
if v not in adj[u]:
    print("Vertices are not adjacent, contraction is impossible")
else:
    contract(adj, u, v)
    print_lists(adj)

s = input("c) Splitting of a vertex. Enter v: ")
v = read_vertex(s, n)
adj = build_lists(m1)
split(adj, v)
print_lists(adj)
