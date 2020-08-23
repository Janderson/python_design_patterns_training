# challenge ad a parameter

import time
import random

def time_it(*args_dec, **kwargs_dec):
    def wrapper(func):
        def wrapped_f(*args_func, **kwargs_func):
            start = time.time()
            print("decorator args -->", *args_dec)

            print("decorator kwargs -->", *kwargs_dec)
            result = func(*args_func, **kwargs_func)
            end = time.time()
            print(f'{func.__name__} took {int((end-start)*1000)}ms')
        return wrapped_f
    return wrapper


@time_it(like= 'as')
def some_op():
    print('Starting op')
    rand_sleep = random.randint(250, 1000) / 1000
    print(rand_sleep)
    time.sleep(rand_sleep)
    print('We are done')
    return 123


if __name__ == "__main__":
    some_op()
    #time_it(some_op)()
