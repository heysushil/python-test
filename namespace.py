# namespace practice
#checkign or teshing only
#what to do

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('inernal a=',a)

    inner_function()
    print('normal inner a=',a)

a = 10
outer_function()
print('outer a=',a)

# next same function with global
def outer_again():
    global a
    a = 30
    def inner_again():
        global a
        a=900
        print('Again inner fun',a)    
    inner_again()
    print('Again out a',a)
a = 10
outer_again()
print('outer noramla a',a)