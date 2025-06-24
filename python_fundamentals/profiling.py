import time

def delayed_task():
    print("Task executed after delay")

delay_time = 10

start_time = time.time()

def executing():
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= delay_time:
            delayed_task()
            break
import cProfile
def my_script():
    executing()
cProfile.run('my_script()')