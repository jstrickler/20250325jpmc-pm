import os
import psutil

class MemoryChecker():
    """
    Callable class to get current memory use of program.

    Instances of this class may be called, at which time
    they will return current memory use.
    """

    def __init__(self):  # constructor
        print("in init")
        self.process = psutil.Process(os.getpid())  # Get PID of current process

    def __call__(self):
        return self.process.memory_info().rss  # Return memory use for PID

if __name__ == '__main__':
    mc = MemoryChecker()
    print(mc())  # can call at any time to get current memory use
    big_array = [0] * 10000000
    print(mc())
    del big_array
    print(mc())
    