def myfunc(n):
  print('myfunb', n)
#   print(a)
  return lambda a: a * n


mydoubler = myfunc(2)
print(type(mydoubler))
print(mydoubler(11))

hello = 1
print(type(hello))
