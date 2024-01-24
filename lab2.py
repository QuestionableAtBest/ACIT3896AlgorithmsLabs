import time
import random

stuff_ten = list(range(10))
stuff_million = list(range(1000000))

d_ten = {str(i): i for i in range(10)}
d_million = {str(i): i for i in range(1000000)}

# Add 1 number to the beginning of a list that already has 10 numbers in it
def add_one_to_ten():
    t0 = time.perf_counter()
    stuff_ten.insert(0, 17)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Add 1 number to the beginning of a list that already has 1,000,000 numbers in it
def add_one_to_million():
    t0 = time.perf_counter()
    stuff_million.insert(0, 203948561123)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Add 1 number to the end of a list that already has 10 numbers in it
def add_one_to_end_ten():
    t0 = time.perf_counter()
    stuff_ten.append(99)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Add 1 number to the end of a list that already has 1,000,000 numbers in it
def add_one_to_end_million():
    t0 = time.perf_counter()
    stuff_million.append(203948561123)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Remove 1 number from the beginning of a list that already has 10 numbers in it
def remove_one_from_ten():
    t0 = time.perf_counter()
    stuff_ten.pop(0)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Remove 1 number from the beginning of a list that already has 1,000,000 numbers in it
def remove_one_from_million():
    t0 = time.perf_counter()
    stuff_million.pop(0)
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Remove 1 number from the end of a list that already has 10 numbers in it
def remove_one_from_end_ten():
    t0 = time.perf_counter()
    stuff_ten.pop()
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Remove 1 number from the end of a list that already has 1,000,000 numbers in it
def remove_one_from_end_million():
    t0 = time.perf_counter()
    stuff_million.pop()
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the presence of a number (9) in a list of 10 numbers
def check_in_list_ten():
    t0 = time.perf_counter()
    _ = random.randint(0, 9) in stuff_ten
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the presence of a number (9) in a list of 1,000,000 numbers
def check_in_list_million():
    t0 = time.perf_counter()
    _ = random.randint(0, 1000000) in stuff_million
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a number (11) in a list of 10 numbers
def check_not_in_list_ten():
    t0 = time.perf_counter()
    _ = 11 not in stuff_ten
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a number (12) in a list of 1,000,000 numbers
def check_not_in_list_million():
    t0 = time.perf_counter()
    _ = 203948561123 not in stuff_million
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the presence of a key ("9") in a dict of 10 key-value pairs
def check_in_dict_ten():
    t0 = time.perf_counter()
    _ = "9" in d_ten
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the presence of a key ("9") in a dict of 1,000,000 key-value pairs
def check_in_dict_million():
    t0 = time.perf_counter()
    _ = "9" in d_million
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a key ("11") in a dict of 10 key-value pairs
def check_not_in_dict_ten():
    t0 = time.perf_counter()
    _ = "11" not in d_ten
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

# Check for the absence of a key ("203948561123") in a dict of 1,000,000 key-value pairs
def check_not_in_dict_million():
    t0 = time.perf_counter()
    _ = "203948561123" not in d_million
    t1 = time.perf_counter()
    return (t1 - t0) * 1e6

def time_average(func):
    time_list = []
    for i in range(50):
        test_time = func()
        time_list.append(test_time)
    # print("All times", time_list) <- Commented out because it's a lot of numbers
    average_time = sum(time_list) / len(time_list)
    print("Average time:", average_time, "microseconds")

# Calling the functions and calculating average times
time_average(add_one_to_ten)
time_average(add_one_to_million)
time_average(add_one_to_end_ten)
time_average(add_one_to_end_million)
time_average(remove_one_from_ten)
time_average(remove_one_from_million)
time_average(remove_one_from_end_ten)
time_average(remove_one_from_end_million)
time_average(check_in_list_ten)
time_average(check_in_list_million)
time_average(check_not_in_list_ten)
time_average(check_not_in_list_million)
time_average(check_in_dict_ten)
time_average(check_in_dict_million)
time_average(check_not_in_dict_ten)
time_average(check_not_in_dict_million)
