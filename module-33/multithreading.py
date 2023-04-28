
# multithreading in python

from time import sleep,perf_counter
from threading import Thread
# task 1
start_time=perf_counter()
def task1():
    for i in range(1,5):
        print(f'Starting task {i}')
        sleep(1)
        print('\n')

def task2():
    for i in range(6,11):
        print(f'Starting task {i}')
        sleep(1)

t1=Thread(target=task1)
t2=Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
end_time=perf_counter()
print(end_time-start_time)

