
from queue import Queue
from time import sleep, perf_counter
from threading import *

start = perf_counter()


def show(argument):
    print(f'start func with arg {argument}')
    sleep(3)
    print(f'end func with arg {argument}')


args_list = [f'string {i}' for i in range(1, 11)]


def create_queue_with_data(data: list | tuple) -> Queue:
    queue = Queue()
    for item in data:
        queue.put(item)
    return queue


def worker(queue):
    while True:
        if queue.empty():
            break
        show(queue.get())


def create_threads(thread_num: int, queue: Queue):
    threads = [Thread(target=worker, args=(queue,)) for _ in range(thread_num)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def main():
    main_queue = create_queue_with_data(args_list)
    create_threads(5, main_queue)


if __name__ == '__main__':
    main()

end = perf_counter()
print(f'total time: {end - start}')
