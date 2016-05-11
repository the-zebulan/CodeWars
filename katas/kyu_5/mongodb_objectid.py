import re
from datetime import datetime

REGEX = re.compile(r'^[a-f\d]{24}$')


class Mongo(object):
    @classmethod
    def is_valid(cls, object_id):
        try:
            return bool(REGEX.match(object_id))
        except TypeError:
            return False

    @classmethod
    def get_timestamp(cls, object_id):
        if cls.is_valid(object_id):
            return datetime.utcfromtimestamp(int(object_id[:8], 16))
        return False
