import time

def timer_v1(func):
    def wrapper(*args):
        tic = time.time()
        result_of_func = func(*args)
        toc = time.time()
        print('--- The function: {} -- {} seconds ---'.format(
              func.__name__, toc-tic))
        return result_of_func
    return wrapper

def timer_v2(t_max):
    # t_max in sec*10^(-2)
    def decorator(func):
        def wrapper(*args):
            tic = time.time()
            result_of_func = func(*args)
            toc = time.time()
            t = toc - tic
            if t-t_max/100 > 0.0001:
                print('--- The function: {} -- OUT OF RANGE({} seconds) ---'.format(
                      func.__name__, t))
            else:
                print('--- The function: {} -- {} seconds ---'.format(
                      func.__name__, t))
            return result_of_func
        return wrapper
    return decorator

def timer_for_generator(func):
    def wrapper(*args):
        tic = time.time()
        result = func(*args)
        yield from result
        toc = time.time()
        print('--- The function: {} -- {} seconds ---'.format(
              func.__name__, toc-tic)
    return wrapper

if __name__ == '__main__':
    @timer_v2(2.5)
    def foo(n):
        for i in range(n):
            print(i+1)
        return('hi')
    
    print(foo(20))
    
    @timer_for_generator
    def gen(n):
        for i in range(n):
            yield i+1
    
    for i in gen(30):
        print(i)
    