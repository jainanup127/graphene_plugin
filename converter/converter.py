import dateutil.parser
from airflow.api.common.experimental import DagRun
from airflow.utils.sqlalchemy import UtcDateTime

def convertDateField(dateString):
     if dateString is None:
          pass
     return dateutil.parser.parse(dateString)

def convertDag(dagRun):
     dr = DagRun()
     dr.__dict__.update(dagRun)
     for col in DagRun.__table__.columns:
          if isinstance(col.type, UtcDateTime):
               if col.name in dagRun.keys():
                    dr.__setattr__(col.name, convertDateField(dagRun[col.name]))
     return dr
