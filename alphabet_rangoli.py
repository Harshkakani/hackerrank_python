x = int(input())
width = (4*x - 3)
alphabets = list(map(chr,range(97,123)))
L = []
for i in range(x):
    s = "-".join(alphabets[i:x])
    L.append((s[::-1]+s[1:]).center(width, "-"))
for i in range(len(L)-1,0,-1):
    print(L[i])

for i in range(len(L)):
    print(L[i])