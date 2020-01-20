from airflow.plugins_manager import AirflowPlugin
from airflow.www.app import csrf
from flask import Blueprint
from flask_graphql import GraphQLView
from graphene import Schema
from graphene_plugin.query_builder.Query import Query

airflow_graphql = Blueprint('airflow_graphql', __name__)
csrf.exempt(airflow_graphql)

airflow_graphql.add_url_rule(
    '/api/airflow',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=Schema(query=Query, auto_camelcase=True),
        graphiql=True
    )
)

class AirflowTestPlugin(AirflowPlugin):
    name = "GraphQLAPI"
    # operators = []
    flask_blueprints = [airflow_graphql]
    # hooks = []
    # executors = []
    #appbuilder_views = [v_appbuilder_package]