from fastapi import APIRouter, Query
from healthdata.waiting_times import get_waiting_time

router = APIRouter()

@router.get("")  # korrekt route: /api/waittimes
def waittime_endpoint(
    treatment: str = Query(..., description="Navn på behandlingen du søker ventetid for"),
    location: str = Query(None, description="Sted eller region (valgfritt)")
):
    return get_waiting_time(treatment, location)
