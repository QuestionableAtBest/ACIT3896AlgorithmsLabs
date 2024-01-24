import time
import random

stuff_ten = list(range(10))
stuff_million = list(range(1000000))

d_ten = {str(i): i for i in range(10)}
d_million = {str(i): i for i in range(1000000)}

# Add 1 number to the beginning of a list that already has 10 numbers in it
def add_one_to_ten():
    t0 = time.perf_counter()
    stuff_ten.insert(0, 1)
    t1 = time.perf_counter()
    print("To add 1 number to the beginning of a list that already has 10 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Add 1 number to the beginning of a list that already has 1,000,000 numbers in it
def add_one_to_million():
    t0 = time.perf_counter()
    stuff_million.insert(0, 1)
    t1 = time.perf_counter()
    print("To add 1 number to the beginning of a list that already has 1,000,000 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Add 1 number to the end of a list that already has 10 numbers in it
def add_one_to_end_ten():
    t0 = time.perf_counter()
    stuff_ten.append(9)
    t1 = time.perf_counter()
    print("To add 1 number to the end of a list that already has 10 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Add 1 number to the end of a list that already has 1,000,000 numbers in it
def add_one_to_end_million():
    t0 = time.perf_counter()
    stuff_million.append(9)
    t1 = time.perf_counter()
    print("To add 1 number to the end of a list that already has 1,000,000 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Remove 1 number from the beginning of a list that already has 10 numbers in it
def remove_one_from_ten():
    t0 = time.perf_counter()
    stuff_ten.pop(0)
    t1 = time.perf_counter()
    print("To remove 1 number from the beginning of a list that already has 10 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Remove 1 number from the beginning of a list that already has 1,000,000 numbers in it
def remove_one_from_million():
    t0 = time.perf_counter()
    stuff_million.pop(0)
    t1 = time.perf_counter()
    print("To remove 1 number from the beginning of a list that already has 1,000,000 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Remove 1 number from the end of a list that already has 10 numbers in it
def remove_one_from_end_ten():
    t0 = time.perf_counter()
    stuff_ten.pop()
    t1 = time.perf_counter()
    print("To remove 1 number from the end of a list that already has 10 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Remove 1 number from the end of a list that already has 1,000,000 numbers in it
def remove_one_from_end_million():
    t0 = time.perf_counter()
    stuff_million.pop()
    t1 = time.perf_counter()
    print("To remove 1 number from the end of a list that already has 1,000,000 numbers in it took:", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a number (9) in a list of 10 numbers
def check_in_list_ten():
    t0 = time.perf_counter()
    if 9 in stuff_ten:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the presence of a number (9) in a list of 10 numbers took:", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a number (9) in a list of 1,000,000 numbers
def check_in_list_million():
    t0 = time.perf_counter()
    if 9 in stuff_million:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the presence of a number (9) in a list of 1,000,000 numbers took:", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a number (9) in a list of 10 numbers
def check_not_in_list_ten():
    t0 = time.perf_counter()
    if 9 not in stuff_ten:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the absence of a number (9) in a list of 10 numbers took:", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a number (9) in a list of 1,000,000 numbers
def check_not_in_list_million():
    t0 = time.perf_counter()
    if 9 not in stuff_million:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the absence of a number (9) in a list of 1,000,000 numbers took:", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a key ("9") in a dict of 10 key-value pairs
def check_in_dict_ten():
    t0 = time.perf_counter()
    if "9" in d_ten:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the presence of a key ('9') in a dict of 10 key-value pairs took:", (t1 - t0) * 1e6, "microseconds")

# Check for the presence of a key ("9") in a dict of 1,000,000 key-value pairs
def check_in_dict_million():
    t0 = time.perf_counter()
    if "9" in d_million:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the presence of a key ('9') in a dict of 1,000,000 key-value pairs took:", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a key ("9") in a dict of 10 key-value pairs
def check_not_in_dict_ten():
    t0 = time.perf_counter()
    if "9" not in d_ten:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the absence of a key ('9') in a dict of 10 key-value pairs took:", (t1 - t0) * 1e6, "microseconds")

# Check for the absence of a key ("9") in a dict of 1,000,000 key-value pairs
def check_not_in_dict_million():
    t0 = time.perf_counter()
    if "9" not in d_million:
        pass  # We just need it to run using Jeremy's syntax
    t1 = time.perf_counter()
    print("To check for the absence of a key ('9') in a dictionary of 1,000,000 key-value pairs took:", (t1 - t0) * 1e6, "microseconds")

# Calling the functions
abc = add_one_to_ten()
add_one_to_million()
add_one_to_end_ten()
add_one_to_end_million()
remove_one_from_ten()
remove_one_from_million()
remove_one_from_end_ten()
remove_one_from_end_million()
check_in_list_ten()
check_in_list_million()
check_not_in_list_ten()
check_not_in_list_million()
check_in_dict_ten()
check_in_dict_million()
check_not_in_dict_ten()
check_not_in_dict_million()
