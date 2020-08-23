import time
import random

def time_it(func):
  def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(f'{func.__name__} took {int((end-start)*1000)}ms')
  return wrapper

@time_it
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
