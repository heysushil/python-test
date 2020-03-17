import constant

print(constant.PI)
print ('hello pyhotn')
name = 'chaudhary'
print(name)
name = 'sushil'
print(name)
print
a = 5
print(a, "is type of", type(a))
a = 5.0
print(a, "is type of", type(a))
a = 1+2j
print(a, "is complex number? ", isinstance(a,int))

# list
a = [1,2,3,4,5,6,7,8,9]
a[1] = 3
print('a[0:2] =',a)

# tubles - this is same as list but it's non changeable but list values area changeable this is the diff
a = (1,2,3,4,5,6)
print(a)
print("values of a[2] is", a[2])
# a[3] = 10
# print(a[3])

# string
a = 'hello python'
print('sting value of a is',a)
print('value of stirng index a[2]', a[0:5])
# a[0] = 'H'
# print('sring also immutable a[0]',a[0])

# set 
# set are not accept 
a = {1,2,3,4,5,'adf',1,2,3,4}
print('look the set',a)
# print('index of a[1]',a[1]) #index not allowed

# directory
newdictonary = {'name':'sushil','address':'nirman vihar'}
print('value of newdirectory',newdictonary)
print(newdictonary['name'])
print(type(newdictonary))

# data type conversion
value = [1, 2, 3, 4, 5]
newconv = list(value)
newconv = tuple(value)
newconv = set(value)
value = ([[1,'hi'],[2,'hello']])
newconv = dict(value)
# newconv = tuple({5,6,7})
print('datatype',type(newconv))
print(newconv)

# fulll print syntex using dictoryny
details = {'name':'Sushil',
            'address':'Nirman vihar',
            'email':'sushil@g.com'
            }
print('Hello {name}, Your Address is {address} and email id is {email} '.format(
    name=details['name'], address=details['address'], email = details['email']))

# input 
# inputnum = eval(input('Enter number: '))
# print('Your entered number is = ',type(inputnum))

# modules breck the code on files and import them 
from math import pi
print(pi)
ca = 12
cb =15
print('Rith or not:',ca<=cb)



# <?php language_attributes(); ?> <?php et_html_tag_schema(); ?> on wp header.php at html tagdsddd
