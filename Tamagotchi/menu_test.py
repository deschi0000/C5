from random import randrange
AWAKE_COMMANDS_SICK = ["f","r", "p", "c", "n" ]



# c = "999"
# while c not in AWAKE_COMMANDS_SICK:
#     c = input("Enter: ")

#/==========================================================


# for i in range(20):
#     print(randrange(0,10))

#/==========================================================

import sys
import time

# def restart_line():
#     sys.stdout.write('\r')
#     sys.stdout.flush()

# sys.stdout.write('some data')
# sys.stdout.flush()
# time.sleep(2) # wait 2 seconds...
# restart_line()
# sys.stdout.write('other different data')
# sys.stdout.flush()

#/==========================================================

# for i in range(5):
#     print(i),
#     #sys.stdout.flush()
#     time.sleep(1)

#/==========================================================


def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()


sys.stdout.write('some data')
sys.stdout.flush()
time.sleep(2) # wait 2 seconds...
restart_line()
sys.stdout.write('other different data')
sys.stdout.flush()
    