# sys use to get exceptions
import sys

rendomList = ['a',0,2]

for num in rendomList:
    try:
        print('Value print is: ',num)
        r = 1/int(num)
        break
    except:
        print('Oppss sys problem: ',sys.exc_info()[0],'occured')
        print('Next entry')
print('The receprocal of',num,'is',r)        


# create class
# parent class
class Birds:

    def __init__(self):
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')
    def swim(self):
        print('Swim faster')

# child class inherit parent calss Birds
class Piggen(Birds):
    
    def __init__(self):
        # call super class
        super.__init__()
        print('Pegun is ready')

    def whoisThis(self):
        print('Pegun is ready')

    

print(Birds().whoisThis())
