import sys
from time import sleep
for i in range(101):
    sys.stdout.write('%2s%%' % i) 
    sys.stdout.flush()
    sleep(0.2)
    sys.stdout.write('\b' * 3)