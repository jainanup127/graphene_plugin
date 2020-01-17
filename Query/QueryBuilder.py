from graphene import ObjectType, String, Boolean, ID, List, Field, Int
from airflow.api.common.experimental.pool import get_pools
from graphene_plugin.Schema.SchemaBuilder import PoolModel


class Query(ObjectType):
    pool = List(PoolModel)

    def resolve_pool(self, context, **kwargs):
        print(get_pools())
        return get_pools()
