'''
Defference b/w list/tuple/set/dic

list - 
    value changeable 
    dublicate values accept
    ordered and indexed
    syntex - []
tupe - 
    value unchangeable
    dublicate value accept
    ordered and indexed
    syntex - ()

set - 
    unordered aur unindexed
    no dublicate value
    syntex - {}

dic - 
    unordered collection value
    indexed
    changeable
    no dublicate
    syntex - {}

-------------------------ABOUT INDEX POSSITIONS---------------------
About - 
    index [] () {}
    index postion - ex - [1]
    negative index - ex - [-1] - last value posstion
    range - [2:5]
    default to range - [:5] - range stope point is 5
    to to last postion - [2:] - 
    negative rang 


'''
# for loop
# i = 0
# for(intialization;i <= 6;i++)
# {
    # for loop body
# }

# newlist = [1,2,3,4,5,6]
# for hello in newlist:
#     print(hello)

# # __len__
# newvaribale = new ClassName()
# newvaribale.functionName()
# this
# self.newlist

# function functionName(newFun())

def funcname(name):
    print('Hello fun, I am',name)

funcname('Python') #argument

newlist = [1,2,3,4,5]
# newlist.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# list1.extend(list2)
print(list1)

list3 = list1+list2
# list1.
print(list3)

tupevalue = ('apple','kiwi','kiwi')
# x = list(tupevalue)
# x[1] = 'manago'
# print(x)
# print(tuple(x))
print(tupevalue.count('apple'))

thisset = {"apple", "banana", "cherry"}

set2 = {"orange", "mango", "grapes","apple"}
print(thisset.union(set2))
# print(thisset.discard('apple'))
# print(thisset)
# ans = thisset+set2
# print(ans)
