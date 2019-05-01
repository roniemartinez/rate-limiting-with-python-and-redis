#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import time

from client import get_redis_client
from exceptions import RateLimitExceeded


def rate_per_second(function, count):
    client = get_redis_client()
    key = f"rate-limit:{int(time.time())}"
    if client.incr(key) > count:
        if client.ttl(key) == -1:  # timeout is not set
            client.expire(key, 1)  # expire in 1 second
        raise RateLimitExceeded
    return function()


def my_function():
    pass  # do something


if __name__ == '__main__':
    success = fail = 0
    for i in range(2000):
        try:
            rate_per_second(my_function, 100)  # example: 100 requests per second
            success += 1
        except RateLimitExceeded:
            fail += 1
        time.sleep(5/1000)  # sleep every 5 milliseconds
    print(f"Success count = {success}")
    print(f"Fail count = {fail}")
