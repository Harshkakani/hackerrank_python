from itertools import groupby

io = input()
for i,j in groupby(map(int,list(io))):
    print(tuple([len(list(j)), i]) ,end = " ")