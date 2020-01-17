from graphene import ObjectType, String, Boolean, ID, List, Field, Int
import json
from graphene import relay
from airflow.models.pool import Pool as Mypool
from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


class PoolModel(ObjectType):
    class Meta:
        model = Mypool
        interfaces = (relay.Node,)

