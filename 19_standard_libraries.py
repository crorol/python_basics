# 1. `math` - related to mathematics
# -----------------------------------------------------------------------------------------------
import math

print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
print(math.pi)             # 3.14159...



# 2. `random` - random number generation
# -----------------------------------------------------------------------------------------------
import random

print(random.randint(1, 10))            # Integer between 1 and 10 (inclusive)
print(random.choice(['a', 'b', 'c']))   # Randomly selects one element from the list
print(random.sample(range(100), 5))     # Picks 5 unique samples from numbers 0 to 99



# 3. `datetime` - handling date and time
# -----------------------------------------------------------------------------------------------
import datetime

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # Print formatted date and time string

from datetime import timedelta

tomorrow = now + timedelta(days=1)
print(tomorrow)



# 4. `os` - operating system interface
# -----------------------------------------------------------------------------------------------
import os

print(os.getcwd())         # Current working directory
print(os.listdir("."))     # List of files and directories in the current directory
# os.mkdir("test_folder")  # Create a new folder named "test_folder"



# 5. `sys` - system paprameters / input and output
# -----------------------------------------------------------------------------------------------
import sys

print(sys.version)   # Python version
print(sys.argv)      # Command-line arguments



# 6. `time` - related to time
# -----------------------------------------------------------------------------------------------
import time

print("Start")
time.sleep(1.5)   # Pause for 1.5 seconds
print("End")



# 7. `collections` - advanced data structures
# -----------------------------------------------------------------------------------------------
from collections import Counter, defaultdict

cnt = Counter("hello")
print(cnt)   # Count the occurrences of each character

dd = defaultdict(int)
dd["a"] += 1
print(dd)    # Automatically creates default values



# 8. `itertools` - utilities for iteration
# -----------------------------------------------------------------------------------------------
from itertools import permutations, combinations

print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), ...]

print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]



# 9. `json` - handling JSON data
# -----------------------------------------------------------------------------------------------
import json

data = {"name": "Daa", "age": 21}
json_str = json.dumps(data)
print(json_str)  # JSON string

parsed = json.loads(json_str)
print(parsed["name"])  # Daa



# 10. `re` - regular expression
# -----------------------------------------------------------------------------------------------
import re

text = "My email is olcror8@gmail.com"
match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print(match.group())   # olcror8@gmail.com



# 11. `urllib` - handling URL
# -----------------------------------------------------------------------------------------------
from urllib.request import urlopen

res = urlopen("https://crorol.com")
print(res.status)
html = res.read().decode("utf-8")
print(html[:200])



# 12. `pathlib` - handling file paths (Python 3.4+)
# -----------------------------------------------------------------------------------------------
from pathlib import Path

p = Path(".")
for file in p.iterdir():
    print(file)



# 13. `statistics` - mean/variance/standard deviation
# -----------------------------------------------------------------------------------------------






# 14. 
# -----------------------------------------------------------------------------------------------





# 15. 
# -----------------------------------------------------------------------------------------------




# 9. 
# -----------------------------------------------------------------------------------------------
