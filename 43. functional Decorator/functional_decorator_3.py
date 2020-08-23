import random
import time
from datetime import datetime

def time_it(*args_dec, **kwargs_dec):
    def wrapper(func):
        def wrapper_func(*args_func, **kwargs_func):
            start = datetime.now()
            print(f"decorator --> args {args_dec}, kwargs {kwargs_dec}")
            print(f"function --> args {args_func}, kwargs {kwargs_func}")
            func(*args_func, **kwargs_func)
            elapsed = (datetime.now() - start).microseconds / 1000
            print(f"elapsed time: {elapsed}")
        return wrapper_func
    return wrapper



@time_it(like= 'as')
def some_op(param1):
    print('Starting op')
    rand_sleep = random.randint(250, 1000) / 1000
    print(rand_sleep)
    time.sleep(rand_sleep)
    print('We are done')
    return 123


if __name__ == "__main__":
    some_op({"teste": 12})
    #time_it(some_op)()
