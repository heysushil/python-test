demolist = [1,2,3,4,5,6,7]
# demolist.remove(1)
print(demolist.count(2))
print(demolist[:])
userdetail = [
    'name','chaudhary suhsil',
    'email','sushil@gmail.com'
]
userdetail[0]='sushil'
userdetail.extend([1,2,3])
# print(count(userdetail))
print(userdetail)

# pworser in case of lsit comparhension
pow2 = [2 ** x for x in range(10)]
print(pow2)

# comperhansion list is awesome
newpow = [2 ** x for x in range(10) if(x > 5)]
print(newpow)

# tuple
# this is called tuple packing
newtup = 3,4.6,'dog'
print(newtup)
# this tuple unpacking
a, b, c = newtup
print(a)
print(b)
print(c)

# string 
count = 0
for letter in 'hello sushil':
    if letter == 'l':
        count += 1
print(count,'letter found')
myname = 'sushil'
myname_enumarate = list(enumerate(myname))
print(myname_enumarate)
print(len(myname))
print('hello, "kyas haal hai"')

# set are mutable and in between set also use all datatypes which are mutable
print(type({1,2,3,4,'hello'}))
print({1,2,3,4})
myset = {'hello','hi','how','areyou'}
print(myset)
myset.add('sushil')
myset.update(['suraj','sunil'])
myset.discard('hi')
myset.remove('how')
print(myset)
# set use for performing mathematical operation 
aset = {1,2,3,4,5}
bset = {5,6,7,8}
print('set union: ',aset|bset)
print('using unio function: ',aset.union(bset))
print('intersion:',aset & bset)
print('using itersetion fun:',aset.intersection(bset))
print('difference:',aset-bset)
print('deferencs fun:',aset.difference(bset))
print('Sementric difference:',aset^bset)
print('semenmtric fun:',aset.symmetric_difference(bset))
print('print in iteration using for:')
for letter in aset:
    print('for loop:',letter)
print('frozen set')
afroz = frozenset([1,2,3,4,5])
bfroz = frozenset([6,7,8,9])
print('disjoint bothe:',afroz.isdisjoint(bfroz))
print('diffrence in frozen:',afroz.difference(bfroz))

# dictonary
print('use of dictornay is same as set but its use key value and use curly backet')
adict = {'name': 'sushil','email':'sushil@gmail.com'}
adict['name'] = 'chaudhary sushil'
adict['mobile'] = '89899889'
print(adict.get('name'))
print(adict)
# print(adict.popitem())
odddict = {x: x*x for x in range(6) if x % 2 == 1}
print({x: x*x for x in range(6) if x%2==1})
print(odddict)
for i in odddict:
    print('In interation:',odddict[i])


