import timeit


def profile(f):
    def time(*args, **kwargs):
        start = timeit.default_timer()
        res = f(*args, **kwargs)
        print(timeit.default_timer() - start)
        return res
    return time


@profile
def some_function():
    return sum(range(10000))


def operate():
    print('===in operation===')


class timer:
    start = 0

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(timeit.default_timer() - self.start)
        return self


result = some_function()

with timer():
    print(sum(range(1000)))
