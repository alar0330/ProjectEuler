from eu001.eu001 import *
from eu002.eu002 import *



print('{task} answer: {ans}'.format(task = eu001.__name__, ans = eu001()))

print('{task} answer: {ans}'.format(task = eu002.__name__, ans = eu002()))
print('{task} answer: {ans}'.format(task = eu002.__name__, ans = sum(eu002_alt(4*1000*1000))))