import graphene
from airflow.api.common.experimental import DagRun,delete_dag as delete
from airflow.api.common.experimental.pool import delete_pool
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

class DeletePool(graphene.Mutation):
    name = graphene.String()
    class Arguments:
        name = graphene.String()
    def mutate(self, info, name):
        return delete_pool(name)

class DeleteDag(graphene.Mutation):
    dagId = graphene.String()
    class Arguments:
        dagId = graphene.String()
    def mutate(self, info, dagId):
        return delete.delete_dag(dagId)

class Mutation(graphene.ObjectType):
    deletePool = DeletePool.Field()
    deleteDag = DeleteDag.Field()