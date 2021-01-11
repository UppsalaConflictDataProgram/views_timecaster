"""
This service converts to and from Vmid (months since 1979-12)
"""
import datetime
import json 

from datetime import date
from typing import Literal,Union,Callable,Any

from dateutil.relativedelta import relativedelta 


from environs import Env
import fastapi
from fastapi.responses import JSONResponse
from pydantic import BaseModel

env = Env()
BASE_DATE = env.date("BASE_DATE","1979-12-01")

app = fastapi.FastAPI()

class DateJsonResponse(JSONResponse):
    @staticmethod
    def _serializerDefaults(o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()

    def render(self, content: Any) -> bytes:
        return json.dumps(content, default=self._serializerDefaults).encode()

class Query(BaseModel):
    origin: Literal["vmid","date"]
    destination: Literal["vmid","date"]
    value: Union[int,date]

class Response(BaseModel):
    value: Union[date,int]
    format: Literal["vmid","date"]

def mid_to_date(mid:int)->date:
    return BASE_DATE + relativedelta(months=mid) 

def date_to_mid(date:date)->int:
    rd = relativedelta(date,BASE_DATE)
    months = rd.months + (rd.years*12)
    return months 

@app.get("/date/{vmid}")
def vmidConv(vmid:int)->date:
    return mid_to_date(vmid)

@app.get("/vmid/{d}")
def dateConv(d:date)->int:
    return date_to_mid(d)
