# Basic threading

from threading import Thread
from time import sleep, perf_counter

def task(_delay: int) -> None:
    print(f"Thread execution started...")
    sleep(_delay)
    print("Thread execution completed.")
    return


delay_list = [2, 5]

start_time = perf_counter()

threads = [Thread(target=task, args=(d,)) for d in delay_list]
[thread.start() for thread in threads]
[thread.join() for thread in threads]

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')