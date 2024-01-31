#Lab link:https://gist.github.com/jholman-bcit/90ef3d4c88acc798b93b5a21d87c5a91

import time
import random

#Add 1 number to the beginning of a list that already has 10 numbers in it
def add_one_to_ten():
    stuff = list(range(10))
    t0 = time.perf_counter()
    stuff.insert(0,9)
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
    end_length = len(stuff) + 1
    t0 = time.perf_counter()
    stuff.insert(end_length, 9)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

#Add 1 number to the end of a list that already has 1,000,000 numbers in it
def add_one_to_end_million():
    stuff = list(range(1000000))
    end_length = len(stuff) + 1
    t0 = time.perf_counter()
    stuff.insert(end_length,9)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

#Remove 1 number from the beginning of a list that already has 10 numbers in it
def remove_one_from_ten():
    stuff = list(range(10))
    t0 = time.perf_counter()
    stuff.pop(0)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

#Remove 1 number from the beginning of a list that already has 1,000,000 numbers in it
def remove_one_from_million():
    stuff = list(range(1000000))
    t0 = time.perf_counter()
    stuff.pop(0)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

#Remove 1 number from the end of a list that already has 10 numbers in it
def remove_one_from_end_ten():
    stuff = list(range(10))
    t0 = time.perf_counter()
    stuff.pop(-1)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

#Add 1 number to the beignning of a list that already has 10 numbers in it
def remove_one_from_end_million():
    stuff = list(range(1000000))
    t0 = time.perf_counter()
    stuff.pop(-1)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6
    
# Check for the presence of a number in a list of 10 numbers
def check_in_list_ten():
    stuff = list(range(10))
    number_to_check = random.randint(0, 20)

    t0 = time.perf_counter()
    if number_to_check in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the presence of a number in a list of 1,000,000 numbers
def check_in_list_million():
    stuff = list(range(1000000))
    number_to_check = random.randint(0, 2000000)

    t0 = time.perf_counter()
    if number_to_check in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a number in a list of 10 numbers
def check_not_in_list_ten():
    stuff = list(range(10))
    number_to_check = random.randint(10, 20)

    t0 = time.perf_counter()
    if number_to_check not in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    return (t1 - t0) * 1e6

# Check for the absence of a number in a list of 1,000,000 numbers
def check_not_in_list_million():
    stuff = list(range(1000000))
    number_to_check = random.randint(0, 2000000)

    t0 = time.perf_counter()
    if number_to_check not in stuff:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    return (t1 - t0) * 1e6


def populate_dict(n):
    d = {}
    for i in range(n):
        d[str(i)] = i
    return d

# Check for the presence of a key in a dict of 10 key-value pairs
def check_in_dict_ten():
    d = populate_dict(10)
    key_to_check = str(random.choice(list(d.keys())))
    t0 = time.perf_counter()
    if key_to_check in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()

    return (t1 - t0) * 1e6

# Check for the presence of a key in a dict of 1,000,000 key-value pairs
def check_in_dict_million():
    d = populate_dict(1000000)
    key_to_check = str(random.choice(list(d.keys())))
    t0 = time.perf_counter()
    if key_to_check in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a key in a dict of 10 key-value pairs
def check_not_in_dict_ten():
    d = populate_dict(10)
    key_to_check = str(random.choice(list(d.keys())))
    t0 = time.perf_counter()
    if key_to_check not in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a key in a dict of 1,000,000 key-value pairs
def check_not_in_dict_million():
    d = populate_dict(1000000)
    key_to_check = str(random.choice(list(d.keys())))
    t0 = time.perf_counter()
    if key_to_check in d:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

def time_average(func):
    time_list = []
    for i in range(50):
        test_time = func()
        time_list.append(test_time)
    # print("All times", time_list) <- Commented out because it's a lot of numbers
    average_time = sum(time_list)/len(time_list)
    print("Average time: ", average_time, "microseconds")
# Calling the functions
# print("Add one to beginning ten")
# time_average(add_one_to_ten)
# print("Add one to beginning million")
# time_average(add_one_to_million)
# print("Add one to end ten")
# time_average(add_one_to_end_ten)
print("Add one to end million")
time_average(add_one_to_end_million)
# print("Remove one from beginning ten")
# time_average(remove_one_from_ten)
# print("Remove one from beginning million")
# time_average(remove_one_from_million)
# print("Remove one from end ten")
# time_average(remove_one_from_end_ten)
# print("Remove one from end million")
# time_average(remove_one_from_end_million)
# print("Check list ten")
# time_average(check_in_list_ten)
# print("Check list million")
# time_average(check_in_list_million)
# print("Check not in list ten")
# time_average(check_not_in_list_ten)
# print("Check not in list million")
# time_average(check_not_in_list_million)
# print("Check in dict ten")
# time_average(check_in_dict_ten)
# print("Check in dict million")
# time_average(check_in_dict_million)
# print("Check not in dict ten")
# time_average(check_not_in_dict_ten)
# print("Check not in dict million")
# time_average(check_not_in_dict_million)


""" 
Harry's Results:
Add one to beginning ten
Average time:  0.21800107788294554 microseconds
Add one to beginning million
Average time:  3387.838003691286 microseconds
Add one to end ten
Average time:  0.4120008088648319 microseconds
Add one to end million
Average time:  2416.3860006956384 microseconds
Remove one from beginning ten
Average time:  0.19200029782950878 microseconds
Remove one from beginning million
Average time:  1267.8300047991797 microseconds
Remove one from end ten
Average time:  0.16600009985268116 microseconds
Remove one from end million
Average time:  2.2099987836554646 microseconds
Check list ten
Average time:  0.19200029782950878 microseconds
Check list million
Average time:  4819.4980004336685 microseconds
Check not in list ten
Average time:  0.19199971575289965 microseconds
Check not in list million
Average time:  4940.400000778027 microseconds
Check in dict ten
Average time:  0.14399935025721788 microseconds
Check in dict million
Average time:  2.526002353988588 microseconds
Check not in dict ten
Average time:  0.1560006057843566 microseconds
Check not in dict million
Average time:  2.342002699151635 microseconds
 """