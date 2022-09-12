from threading import Thread, Lock, current_thread
from queue import Queue
import time


database_value = 0


def increase(lock):
    global database_value

    # lock.acquire()
    with lock:
        local_copy = database_value

        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
    # lock.release()


def worker(q, lock):
    while True:
        value = q.get()

        # processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


def square_numbers():
    for i in range(100):
        i * i


if __name__ == '__main__':
    # lock = Lock()
    # print('Start value', database_value)
    
    # thread1 = Thread(target=increase, args=(lock,))
    # thread2 = Thread(target=increase, args=(lock,))

    # thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()

    # print('End value', database_value)

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3 2 1 -->
    # first = q.get()
    # print(first)
    # q.task_done()
    # q.join()

    # threads = []
    # num_threads = 10

    # # create threads
    # for i in range(num_threads):
    #     thread = Thread(target=square_numbers)
    #     threads.append(thread)

    # # start threads
    # for thread in threads:
    #     thread.start()

    # # join threads: wait for them to complete
    # for thread in threads:
    #     thread.join()

    print('End main')
