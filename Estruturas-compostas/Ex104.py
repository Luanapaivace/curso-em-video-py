def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    return r

resp = notas(5.5, 2.3, 10, 6.7)
print(resp)