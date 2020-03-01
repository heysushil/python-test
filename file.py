print('File operations')
# f = open('file.txt')
# print('Is file open:',f)
# newf = open('hello.txt', mode='a')
# print('Create new file hello.txt:',newf)
# f.close()
# newf.close()

# use safe mode avop mode is not safe on so use tye filan
try:
    f = open('file.txt')
    # best way to use the is - with 
    
    with open('file.txt',mode='w') as f:
        f.write('kya baat hai maza hi aa gaya. mast hai python hain na\n')
        f.write('ye jo bate hai ye to hoti hi rangei\n\n')
        f.write('magar agar kaha jaye to maja aata hai python me aur hai hi majedat')
        # f.write('this is my first file\n')
        # f.write('no problem to wirht here\n')
        # f.write('it\'s great idea to writh in the file by python.\n\n')
        # f.write('really awesome')        
    # with open('file.txt','r') as f:
    #     print(f)

    # newf = open('hello.txt',mode='a')
    # print('created file:',f)
    # print('Create new file using a:',newf)
finally:
    f.close()
    # newf.close()

# read('file.txt')
readfile = open('file.txt','r')
print(open('file.txt', 'r').read())
print('current file position:',readfile.tell())
print('bright currsor to initial posion',readfile.seek(0))

# read file in loop
print('\n\n')
for i in readfile:
    print(i,end='')  #end use to stope reapeting double new line

print(readfile.readline())
