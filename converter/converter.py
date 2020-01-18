#!/usr/bin/env python3

from graphene.types.resolver import dict_resolver
from airflow.api.common.experimental import DagRun

def convertDag(dagRun):
     p = DagRun()
     p.__dict__.update(dagRun)
     return p
