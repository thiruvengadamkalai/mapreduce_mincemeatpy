import mincemeat
from sys import argv

script, given = argv
data = given;

datasource = dict(given = data)


def mapfn(k, v):
    import hashlib
    import string
    import itertools

    allchar = list(string.ascii_lowercase + string.digits)
    allcomb = []

    for i in range(1,5):
        allcomb.extend(itertools.permutations(allchar, i))

    for w in allcomb:
        pswrd = ''.join(w)
        if hashlib.md5(pswrd).hexdigest()[:5] == v:
            yield 'found', pswrd

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn


results = s.run_server(password="changeme")
print results

