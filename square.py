num = 8
sqr_num = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num, sqr_num))

num = 2
print(num**3)

# Find square root of real or complex numbers
# Importing the complex math module

import cmath as cm

num = 1+2j
num_sqr = cm.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}'.format(num, num_sqr.real, num_sqr.imag))