from fastapi import APIRouter, Query
from ..healthdata.waiting_times import get_waiting_time

router = APIRouter()

@router.get("")
def waittime_endpoint(
    treatment: str = Query(..., description="Behandling"),
    location: str = Query(None, description="Sted (valgfritt
