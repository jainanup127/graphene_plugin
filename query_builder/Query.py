import graphene_plugin.converter.converter as Converter
from airflow.api.common.experimental.get_dag_runs import get_dag_runs
from airflow.api.common.experimental.pool import get_pools
from graphene import ObjectType, List, String
from graphene_plugin.schema_generator.SchemaBuilder import PoolModel, DagRunModel

class Query(ObjectType):
    pools = List(PoolModel)
    all_dagruns = List(DagRunModel, dagId = String(required=True))

    def resolve_pools(self, info,**kwargs):
        return get_pools()

    def resolve_all_dagruns(self, info, dagId):
        dagruns = get_dag_runs(dagId, run_url_route="airflow.graph")
        new_list = list(Converter.convertDag(dictionary) for dictionary in dagruns)
        return new_list

