import graphene_sqlalchemy.converter as converter
from airflow.utils.sqlalchemy import UtcDateTime, Interval
from graphene import String


@converter.convert_sqlalchemy_type.register(UtcDateTime)
def convert_column_to_datetime(type, column, registry=None):
    from graphene.types.datetime import DateTime
    return DateTime

@converter.convert_sqlalchemy_type.register(Interval)
def convert_column_to_string(type, column, registry=None):
    return String