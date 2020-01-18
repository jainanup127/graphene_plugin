from airflow.api.common.experimental import DagRun
from airflow.models.pool import Pool
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

class PoolModel(SQLAlchemyObjectType):
    class Meta:
        model = Pool
        interfaces = (relay.Node,)
        exclude_fields = ('conf')

class DagRunModel(SQLAlchemyObjectType):
    class Meta:
        model = DagRun
        interfaces = (relay.Node,)
        exclude_fields = ('conf')