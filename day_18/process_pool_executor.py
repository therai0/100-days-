""" 
multiprocessing can be implemented using the ProcessPoolExecutor from the concurrent.futures module. This executor manages multiple processes, allowing parallel execution across CPU cores.
"""


from concurrent.futures import ProcessPoolExecutor
import time

def  print_cube(number):
    time.sleep(2)
    return number*number*number

numbers = [x for x in range(10)]
if __name__ == "__main__":
# # This condition checks whether the current script is being run directly (not imported as a module in another script). creating multiple process of function
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_cube, numbers)
    start_time = time.time()
    for num in results:
        print(f"Cube numbers:{num}")
    end_time = time.time()-start_time

    print(f"Total time:{end_time}")
# output:
# Cube numbers:0
# Cube numbers:1
# Cube numbers:8
# Cube numbers:27
# Cube numbers:64
# Cube numbers:125
# Cube numbers:216
# Cube numbers:343
# Cube numbers:512
# Cube numbers:729
# Total time:0.00013113021850585938