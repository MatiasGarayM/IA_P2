def modus_ponens(p, q):
    if p:
        return q
p = True
q = False
print(modus_ponens(p, q))