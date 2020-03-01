# loop in python using 2 paremeters 
# first is the variable which initialize before start
# second is the sequesnce in which the loop rounding
# like in py use a list,tuple,dictroney, string which provide many number of values

# --------------------------------------------------------------------
# ----------------FINAL ABOUT LOOP----------------------
# -----------------------------------------------------------------------
# loop is using only 2 parametres on loop case in for loop firs is the initialization value wich you can direct initialize here no need to initialize before and next the the way of how the loop itirate the same for the time .
# in this case on simple case on 2nd paremeter pass the list,dictonary,string value of repet the loop until not finish the value on these.
# on other side if we want to repeate the loop for same type of number like print 0 to 100 number in loop. In this casea py provides a range() predefine function which you also use direct without use of loop in just print case
# but on print case it use also if you want to use the sam ein case of loop then everything work same just change the second paremeter.
# like for initialize-value in list-value:
# in this case the list-value will use in range and in rage also use len-for get the length of the list to repect the loop untile get the end value
# in this case the for loop lookes like
# for i in range(len(itemsvalue))

# list of number
listnum = ['hello','hai','how','are','you']
# print(len(listnum))

for i in range(len(listnum)):
    print(listnum[i])

# print(list(range(0,10)))
# print(list(range(0,100)))
digit = [1,2,3]
for hello in digit:
    print(hello)
    # continue
else:
    print('No item left')   

# ----------------------------------
#  WHILE LOOP
n = 10
sum = 0
i=1
while i <= n:
    sum = sum + i
    # print(len(n))
    i = i+1
print('get',sum)

# whicle with else
counter = 0
while counter < 3:
    print('get counter')
    counter = counter+1
else:
    print('stop counter')

for val in 'string':
    if val == 'i':
        continue
    print(val)
        # break
else:
    print('finshed string')

# function
def simplefun(name):
    return 'Hello, ' + name + ' how are you.'
    # return 

print (simplefun('Roshan')) 

# lambda function
oldlist = [1,2,3,4,5,6,7,8,9]
newlist = list(map(lambda x: x*2, oldlist))
print('New list is: ',newlist)


