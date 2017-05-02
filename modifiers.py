# universal modifiers for functions
# functools' wraps preserves any names and (future) docstrings of original functions when called with decorators

from functools import wraps
import time

# import logging
# import sys

# from ratelimiter import RateLimiter


def timed(func):
    @wraps(func)
    def timer(*args, **kwargs):
        before = time.time()
        f_result = func(*args, **kwargs)
        duration = round(time.time() - before, 8)
        print('{} | {} called with args {} and kwargs {!r}'.format(duration, func.__name__, args, kwargs))
        return f_result
    return timer


def logged():
    pass


# TO DO: try to make this thread-safe for async behaviour in future code elsewhere, because this uses time.sleep()
def rate_limited(max_per_sec):
    # Refactored from: http://stackoverflow.com/a/667706
    # Used under the MIT License with reasonable attribution as per Stack Overflow policy dating 2016-03-01.
    min_interval = 1.0 / float(max_per_sec)

    def limit(func):
        before = [0.0]

        @wraps(func)
        def force_wait(*args, **kwargs):
            duration = time.time() - before[0]
            wait_time = min_interval - duration
            if wait_time > 0:
                time.sleep(wait_time)
            f_result = func(*args, **kwargs)
            before[0] = time.time()
            return f_result
        return force_wait
    return limit
