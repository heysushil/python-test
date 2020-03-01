# decoratores are nothing more then assing value of variables.
# because in this case the decoratore means is to assign the calling function to a variable which holds that function on it.
# it also call as short hand the fucntion with define a new name to call same function by different name for different functions
# same case we done in class, when we have class so for using the class need to creat an object of it and we create as many as object as we want of the same class.
# in case of decoration same done by like class object
# short hand for the decorate is
'''
    Exampele to shor hand way use of decoratoer
    @make_pretty
    def ordinary():
        print("I am ordinary")
    is equivalent to

    def ordinary():
        print("I am ordinary")
    ordinary = make_pretty(ordinary)

    --------------use of multiple decoratore-------------
    Example: 
        def star(func):
            def inner(*args, **kwargs):
                print("*" * 30)
                func(*args, **kwargs)
                print("*" * 30)
            return inner

        def percent(func):
            def inner(*args, **kwargs):
                print("%" * 30)
                func(*args, **kwargs)
                print("%" * 30)
            return inner

        @star
        @percent
        def printer(msg):
            print(msg)
        printer("Hello")
'''

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

    # def is_newmess():
    #     print('Hello other sub functon')
    # return is_newmess

new = is_called()

#Outputs "Hello"
new()
