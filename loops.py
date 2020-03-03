# intilization
# condition
# increment / decrement

for i in range(5):
    for j in range(i):
        print(j)
print('\n')

# for(intialization;condtion;increment)
# {
#     //loop body
# }
# for i in range(1,11):
# for(i=0;i<8;i++)
# {
#     //body
# }

# intilization
# while(condtion)
# {
#     //loop body
#     increment / decreent
# }

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# i is value initialization
# range or list or tupel or set or dict all are provide indexs or end point of loop
for i in range(-11,-1):
    print(i)

# num1 = int(input('Enmter fir number'))
# num2 = int(input('Enter second number'))
# print(type(num1))
# print(type(num2))
# sum = num1+num2
# print(sum)
a = 1
while a < 10:
    print('A : ',a)
    a = a+1

# with if 
b = 10
while b <= 20:
    b += 1  # -- ++
    if b == 13:
        continue
    print('B is: ', b)
# decrement
dec = 20
while dec > 0:
    print('Dec value: ',dec)
    dec = dec - 4

print('--------------------------')
mul1 = int(input('Enter number'))
mul = 1
for mul in range(1,10, 2):
    # print('Mul: ',mul1*mul)
    print('Multip {0}'.format(mul1))
    mul += 1
else:
    print('{0} multiplication stop'.format(mul1))

num = 1
while num > 5:
    print('IN while loop')
else:
    while num < 5:
        print('Num: ',num)
        num +=1

name = 'Vanshika'
print(name[1])

# for i in range():
    # pass
# while

