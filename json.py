import simplejson

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = simplejson.loads(x)

# the result is a Python dictionary:
print(y["age"])

print('Hello hi how are you',sep="/")
raise 