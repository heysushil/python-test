a = 5
name = 'Vanshika'
if a > 5:
    print('Value of a: ',name)
# elif a >= 5:
#     if name == 'Vaknshika':
#         print('Hello - {0}, welcome to python'.format(name))
#     if a >= 5:
#         print('Vlaue of a is {0}.'.format(a))
else:
    pass
    # print('Not greate a')


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
if a > b:
    print("A")
else:
    if a < b:
        print("=")
    else:
        print("B")