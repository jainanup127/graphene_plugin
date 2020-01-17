
from graphene_plugin.Query.QueryBuilder import Query as qs
from airflow.www.app import csrf
from flask_graphql import GraphQLView
from graphene import Schema
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint,session

test_experiment2 = Blueprint('test_experiment2', __name__)
test_experiment2.add_url_rule(
    '/api/test1',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=Schema(query=qs),
        graphiql=True
    )
)

csrf.exempt(test_experiment2)

class AirflowTestPlugin(AirflowPlugin):
    name = "GraphQLAPIsv2"
    # operators = []
    flask_blueprints = [test_experiment2]
    # hooks = []
    # executors = []
    #appbuilder_views = [v_appbuilder_package]