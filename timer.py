import time

def timer_v1(func):
    def wrapper(*args):
        tic = time.time()
        func(*args)
        toc = time.time()
        print('--- The function: {} -- {} seconds ---'.format(
              func.__name__, toc-tic))
    return wrapper

def timer_v2(t_max):
    # t_max in sec*10^(-2)
    def decorator(func):
        def wrapper(*args):
            tic = time.time()
            func(*args)
            toc = time.time()
            t = toc - tic
            if t-t_max/100 > 0.0001:
                print('--- The function: {} -- OUT OF RANGE({} seconds) ---'.format(
                      func.__name__, t))
            else:
                print('--- The function: {} -- {} seconds ---'.format(
                      func.__name__, t))
        return wrapper
    return decorator

if __name__ == '__main__':
    @timer_v2(2.5)
    def foo(n):
        for i in range(n):
            print(i+1)
    foo(20)
    