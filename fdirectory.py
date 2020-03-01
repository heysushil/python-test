import os

os.getcwd()
print(os.getcwdb())
print(os.listdir())
# print(check)
# print(os.mkdir('testdir'))
print(os.listdir())
# os.mkdir('testdir')
# create file in directory
fname = open('testdir/text.txt', 'a')
fwrite = open('testdir/text.txt','w')
fwrite.write('Hello sushil how are you\nthis is firs directory inccer page')
# read the file
# fread = open('testdir/text.txt','r')
print(open('testdir/text.txt', 'r').read())
# print(os.remove('testdir/text.txt'))

# use shutil modul to delete non empty dierecoty
import shutil
shutil.rmtree('testdir')
# fname.write = 'hello sushil\nthis is a dmeo file which i just created ok.'
# print(fname.read())
# print(os.rename('testdir','newtest'))
# print(os.rmdir('newtest'))
print(os.listdir())

def funcname():
    pass

# function functionName(){
#     function body
# }
a = '1'
b = 1
print(a)
