import functools

floats = [5,4,3,2,1]


reduced = functools.reduce(lambda x,y:x*y,floats)
print(reduced)
