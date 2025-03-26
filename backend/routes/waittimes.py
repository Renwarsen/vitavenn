
from fastapi import APIRouter, Query
from healthdata.waiting_times import get_waiting_time

router = APIRouter()

@router.get("/api/waittimes")
def waittime_endpoint(treatment: str, location: str = None):
    return get_waiting_time(treatment, location)
