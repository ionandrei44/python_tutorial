from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())

    a = Process(target=counter, args=(500000,))
    b = Process(target=counter, args=(500000,))

    a.start()
    b.start()

    a.join()
    b.join()
    print("finished in: ", time.process_time())


if __name__ == "__main__":
    main()
