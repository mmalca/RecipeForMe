import json


class JsonToObject(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


class ObjectToJson(object):
    def __init__(self, obj):
        json.dumps(obj.__dict__)


class Recipe:
    def __init__(self, name, id):
        self.name = name
        self.processor = id

    def object_to_json(self):
        str = json.dumps(self.__dict__)
        return str
