#Lab link:https://gist.github.com/jholman-bcit/90ef3d4c88acc798b93b5a21d87c5a91

import time
import random

#Add 1 number to the beginning of a list that already has 10 numbers in it
def add_one_to_ten():
    stuff = list(range(10))
    end_length = len(stuff) + 1

    t0 = time.perf_counter()
    stuff.insert(9,end_length)
    t1 = time.perf_counter()
    
    return (t1 - t0) * 1e6

#Add 1 number to the beginning of a list that already has 1,000,000 numbers in it
def add_one_to_million():
    stuff = list(range(1000000))

    t0 = time.perf_counter()
    stuff.insert(0, 9)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

#Add 1 number to the end of a list that already has 10 numbers in it
def add_one_to_end_ten():
    stuff = list(range(10))

    t0 = time.perf_counter()
    stuff.append(9)
    t1 = time.perf_counter()
    print("To add 1 number to the end of a list that already has 10 numbers in it took: ", (t1 - t0) * 1e6, "microseconds")

#Add 1 number to the end of a list that already has 1,000,000 numbers in it
def add_one_to_end_million():
    stuff = list(range(1000000))

    t0 = time.perf_counter()
    stuff.append(random.randint(1000001, 2000000))
    t1 = time.perf_counter()
    print("To add 1 number to the end of a list that already has 1,000,000 numbers in it took: ", (t1 - t0) * 1e6, "microseconds")

#Remove 1 number from the beginning of a list that already has 10 numbers in it
def remove_one_from_ten():
    stuff = list(range(10))

    t0 = time.perf_counter()
    stuff.pop(0)
    t1 = time.perf_counter()
    print("To remove 1 number from the beginning of a list that already has 10 numbers in it took: ", (t1 - t0) * 1e6, "microseconds")

#Remove 1 number from the beginning of a list that already has 1,000,000 numbers in it
def remove_one_from_million():
    stuff = list(range(1000000))

    t0 = time.perf_counter()
    stuff.pop(0)
    t1 = time.perf_counter()
    print("To remove 1 number from the beginning of a list that already has 1000000 numbers in it took: ", (t1 - t0) * 1e6, "microseconds")

#Remove 1 number from the end of a list that already has 10 numbers in it
def remove_one_from_end_ten():
    stuff = list(range(10))
    t0 = time.perf_counter()
    stuff.pop()
    t1 = time.perf_counter()
    print("To remove 1 number from the end of a list that already has 10 numbers in it took: ", (t1 - t0) * 1e6, "microseconds")

#Add 1 number to the beignning of a list that already has 10 numbers in it
def remove_one_from_end_million():
    stuff = list(range(1000000))
    t0 = time.perf_counter()
    stuff.pop()
    t1 = time.perf_counter()
    print("To remove 1 number from the end of a list that already has 1,000,000 numbers in it took: ", (t1 - t0) * 1e6, "microseconds")
    
# Check for the presence of a number in a list of 10 numbers
def check_in_list_ten():
    stuff = list(range(10))
    number_to_check = random.randint(0, 9)

    t0 = time.perf_counter()
    if number_to_check in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the presence of a number in a list of 10 numbers took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a number in a list of 1,000,000 numbers
def check_in_list_million():
    stuff = list(range(1000000))
    number_to_check = random.randint(0, 999999)

    t0 = time.perf_counter()
    if number_to_check in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the presence of a number in a list of 1,000,000 numbers took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a number in a list of 10 numbers
def check_not_in_list_ten():
    stuff = list(range(10))
    number_to_check = random.randint(10, 20)

    t0 = time.perf_counter()
    if number_to_check not in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the absence of a number in a list of 10 numbers took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a number in a list of 1,000,000 numbers
def check_not_in_list_million():
    stuff = list(range(1000000))
    number_to_check = random.randint(1000001, 2000000)

    t0 = time.perf_counter()
    if number_to_check not in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the absence of a number in a list of 1,000,000 numbers took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a key in a dict of 10 key-value pairs
def check_in_dict_ten():
    d = {str(i): i for i in range(10)}
    key_to_check = str(random.randint(0, 9))

    t0 = time.perf_counter()
    if key_to_check in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the presence of a key in a dict of 10 key-value pairs took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a key in a dict of 1,000,000 key-value pairs
def check_in_dict_million():
    d = {str(i): i for i in range(1000000)}
    key_to_check = str(random.randint(0, 999999))

    t0 = time.perf_counter()
    if key_to_check in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the presence of a key in a dict of 1,000,000 key-value pairs took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a key in a dict of 10 key-value pairs
def check_not_in_dict_ten():
    d = {str(i): i for i in range(10)}
    key_to_check = str(random.randint(10, 20))

    t0 = time.perf_counter()
    if key_to_check not in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the absence of a key in a dict of 10 key-value pairs took: ", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a key in a dict of 1,000,000 key-value pairs
def check_not_in_dict_million():
    d = {str(i): i for i in range(1000000)}
    key_to_check = str(random.randint(1000001, 2000000))

    t0 = time.perf_counter()
    if key_to_check not in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    print("To check for the absence of a key in a dictionary of 1,000,000 key-value pairs took: ", (t1 - t0) * 1e6, "microseconds")

def time_average(func):
    time_list = []
    for i in range(50):
        test_time = func()
        time_list.append(test_time)
    # print("All times", time_list) <- Commented out because it's a lot of numbers
    average_time = sum(time_list)/len(time_list)
    print("Average time: ", average_time, "microseconds")
# Calling the functions
time_average(add_one_to_ten)
time_average(add_one_to_million)
# add_one_to_million()
# add_one_to_end_ten()
# add_one_to_end_million()
# remove_one_from_ten()
# remove_one_from_million()
# remove_one_from_end_ten()
# remove_one_from_end_million()
# check_in_list_ten()
# check_in_list_million()
# check_not_in_list_ten()
# check_not_in_list_million()
# check_in_dict_ten()
# check_in_dict_million()
# check_not_in_dict_ten()
# check_not_in_dict_million()
