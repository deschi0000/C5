import time
import os
from frame_functions import *

def death_animation():
    # print("It died")
    time.sleep(2)

    for i in range(0, 3):
        os.system("cls")
        ghost_1()
        time.sleep(1.2)
        os.system("cls")
        ghost_2()
        time.sleep(1)
    os.system("cls")

def eat_animation():
    for i in range(0, 5):
        os.system("cls")
        eat_1()
        time.sleep(0.6)
        os.system("cls")
        eat_2()
        time.sleep(0.6)
    # os.system("cls")


def sleep_animation():
    for i in range(0, 2):
        os.system("cls")
        sleep_1()
        time.sleep(0.8)
        os.system("cls")
        sleep_2()
        time.sleep(0.8)
    # os.system("cls")

def unchi_animation():
    for i in range(0, 3):
        os.system("cls")
        unchi_1()
        time.sleep(0.9)
        os.system("cls")
        unchi_2()
        time.sleep(0.9)
    # os.system("cls")


def happy_animation():
    os.system("cls")
    happy_1()
    time.sleep(3)
    # os.system("cls")

def wake_up_animation():
    os.system("cls")
    wake_up1()
    time.sleep(3)
    # os.system("cls")

def unclean_animation():
    os.system("cls")
    unclean_1()
    time.sleep(3)
    # os.system("cls")

def sick_animation():
    os.system("cls")
    sick_1()
    time.sleep(3)
    # os.system("cls")
    

def sick_animation2():
    for i in range(0, 3):
        os.system("cls")
        sick_2()
        time.sleep(0.9)
        os.system("cls")
        sick_3()
        time.sleep(0.9)

# eat_animation()
# death_animation()
# sleep_animation()
# unchi_animation()
# happy_animation()
# sick_animation()
# sick_animation2()
# wake_up_animation()
# unclean_animation()
