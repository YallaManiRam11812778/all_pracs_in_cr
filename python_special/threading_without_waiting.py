# import threading
# def waitForASec():
#     count = 0
#     while(count < 100000000):
#         count +=1

#     print("hello world")

# def main_process():
#     t1 = threading.Thread(target=waitForASec, name='t1')
#     t1.start()
#     return "cool"

# print(main_process())
import threading
import time

def batch_process_thread(i):
    print(f"Thread {i} started")
    time.sleep(2)  # Simulates a delay
    if i == 2:
        time.sleep(4)
    print(f"Thread {i} finished")

# Simulating a list of invoice numbers
invoice_nos_list = [1, 2, 3]

for i in invoice_nos_list:
    t = threading.Thread(target=batch_process_thread, args=(i,))
    t.start()

print("Main thread continues to run independently.")
