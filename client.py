#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import os

import redis

redis_client = None


def get_redis_client():
    global redis_client
    if not redis_client:
        # get credentials from environment variables
        redis_client = redis.Redis(
            host=os.getenv('REDIS_HOST'),
            port=os.getenv('REDIS_PORT'),
            db=os.getenv('REDIS_DB'),
            password=os.getenv('REDIS_PASSWORD')
        )
    assert redis_client.ping()
    return redis_client
