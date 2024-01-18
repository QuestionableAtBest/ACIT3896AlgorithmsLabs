#Lab link:https://gist.github.com/jholman-bcit/90ef3d4c88acc798b93b5a21d87c5a91

import time
import random

#Add 1 number to the beginning of a list that already has 10 numbers in it
def add_one_to_ten():
    stuff = list(range(10))

    t0 = time.perf_counter()
    stuff.insert(0, random.randint(11, 20))
    t1 = time.perf_counter()
    
    print("To add 1 number to the beginning of a list that already has 10 numbers in it took: ", t1-t0, "seconds")
#Paul's times:
#Harry's times:

#Add 1 number to the beginning of a list that already has 1,000,000 numbers in it
def add_one_to_million():
    stuff = list(range(1000000))

    t0 = time.perf_counter()
    stuff.insert(0, random.randint(1000001, 2000000))
    t1 = time.perf_counter()
    print("To add 1 number to the beginning of a list that already has 1,000,000 numbers in it took: ", t1-t0, "seconds")
#Paul's times:
#Harry's times:

#Add 1 number to the end of a list that already has 10 numbers in it
def add_one_to_end_ten():
    stuff = list(range(10))

    t0 = time.perf_counter()
    stuff.append(random.randint(11, 20))
    t1 = time.perf_counter()
    print("To add 1 number to the end of a list that already has 10 numbers in it took: ", t1-t0, "seconds")
#Paul's times:
#Harry's times:

#Add 1 number to the end of a list that already has 1,000,000 numbers in it
def add_one_to_end_million():
    stuff = list(range(1000000))

    t0 = time.perf_counter()
    stuff.append(random.randint(1000001, 2000000))
    t1 = time.perf_counter()
    print("To add 1 number to the end of a list that already has 1,000,000 numbers in it took: ", t1-t0, "seconds")
#Paul's times:
#Harry's times:

#Remove 1 number from the beginning of a list that already has 10 numbers in it
def remove_one_from_ten():
    stuff = list(range(10))

    t0 = time.perf_counter()
    stuff.pop(0)
    t1 = time.perf_counter()
    print("To remove 1 number from the beginning of a list that already has 10 numbers in it took: ", t1-t0, "seconds")
#Paul's times:
#Harry's times:

#Remove 1 number from the beginning of a list that already has 1,000,000 numbers in it
def remove_one_from_million():
    stuff = list(range(1000000))

    t0 = time.perf_counter()
    stuff.pop(0)
    t1 = time.perf_counter()
    print("To remove 1 number from the beginning of a list that already has 1000000 numbers in it took: ", t1-t0, "seconds")

#Paul's times:
#Harry's times:

#Remove 1 number from the end of a list that already has 10 numbers in it
def remove_one_from_end_ten():
    stuff = list(range(10))
    t0 = time.perf_counter()
    stuff.pop()
    t1 = time.perf_counter()
    print("To remove 1 number from the end of a list that already has 10 numbers in it took: ", t1-t0, "seconds")
    pass
#Paul's times:
#Harry's times:

#Add 1 number to the beignning of a list that already has 10 numbers in it
def remove_one_from_end_million():
    stuff = list(range(1000000))
    t0 = time.perf_counter()
    stuff.pop()
    t1 = time.perf_counter()
    print("To remove 1 number from the end of a list that already has 1,000,000 numbers in it took: ", t1-t0, "seconds")
#Paul's times:
#Harry's times: