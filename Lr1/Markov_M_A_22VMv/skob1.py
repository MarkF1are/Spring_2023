x = input("")
s = None
d = None
for i, v in enumerate(x):
    if v == "(":
        s = i
    elif v == ")":
        d = i
f = x[s+1:d]
print(f)