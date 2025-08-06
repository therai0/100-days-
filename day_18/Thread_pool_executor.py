"""
The Python ProcessPoolExecutor allows us to create and manage process pools in Python
"""

# importing processs pool executor 
from  concurrent.futures import ThreadPoolExecutor
import time
# function which returns the username
def print_username(username):
    time.sleep(2)
    return  f"Hi {username}"

username = ["bhaskar","Manish","Aayush","Jemish","Bishal"]
with ThreadPoolExecutor(max_workers=3)as executor:  # creating the threadpool
    #max_workers = 3 means 3 threads at a same time
    results = executor.map(print_username,username)
# The function print_username() will run in parallel (concurrently) on up to 3 items at a time — because of max_workers=3.
start_time = time.time()
for name in results:
    print(name)
end_time = time.time() - start_time
print(f"Total time:{end_time}")
# output:
# Hi bhaskar
# Hi Manish
# Hi Aayush
# Hi Jemish
# Hi Bishal
# Total time:0.00014591217041015625