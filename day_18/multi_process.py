# Multiprocessing implementation with function
import multiprocessing
import time
# function one
def  print_odd():
    for i in range(10):
        if i % 2 != 0:
            time.sleep(1)
            print(f"Print odd:{i}")
# function two
def print_even():
    for i in range(10):
        if i % 2 == 0:
            time.sleep(2)
            print(f"Print even:{i}")

if __name__ == "__main__": # This condition checks whether the current script is being run directly (not imported as a module in another script).
    # creating multiple process of function
    process_one = multiprocessing.Process(target=print_odd)
    process_two = multiprocessing.Process(target=print_even)
    # starting the both process
    start_time = time.time()
    process_one.start()
    process_two.start()
    # To ensure both processes complete before moving on, we use the join() method.
    process_one.join()
    process_two.join()

    total_time = time.time() - start_time
    print(f"Total time:{total_time}")

# output:
# Print odd:1
# Print odd:3
# Print even:0
# Print odd:5
# Print odd:7
# Print even:2
# Print odd:9
# Print even:4
# Print even:6
# Print even:8
# Total time:10.0902578830719
