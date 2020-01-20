from airflow.api.common.experimental import DagRun
from airflow.models.pool import Pool
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

class PoolModel(SQLAlchemyObjectType):
    class Meta:
        model = Pool
        interfaces = (relay.Node,)

class DagRunModel(SQLAlchemyObjectType):
    class Meta:
        model = DagRun
        interfaces = (relay.Node,)
        only_fields = ("id","run_id","_state","dag_id","execution_date","start_date")
        #exclude_fields = ('conf')
