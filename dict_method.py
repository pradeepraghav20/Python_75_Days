print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
d={1:4,4:5,6:33}
print(d)
print(d.get(1))
d.pop(1)
print(d)
d[44]=44
print(d)
d.popitem()
print(d)
d2={"name":'pradeep'}
d.update(d2)
print(d)

# d.fromkeys()
print ({}.fromkeys(range(1,12),20))
print(d.setdefault("s_name","amit"))

print(d)

