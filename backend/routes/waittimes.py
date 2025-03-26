from fastapi import APIRouter, Query
from ..healthdata.waiting_times import get_waiting_time

router = APIRouter()

@router.get("")
def waittime_endpoint(
    treatment: str = Query(..., description="Behandling"),
    location: str = Query(None, description="Sted (valgfritt)")):
    # Her kaller vi på get_waiting_time-funksjonen for å hente ventetiden
    try:
        wait_time = get_waiting_time(treatment, location)  # Antar at denne funksjonen returnerer ventetiden
        return {"treatment": treatment, "location": location, "wait_time": wait_time}
    except Exception as e:
        return {"error": str(e), "message": "Noe gikk galt ved henting av ventetid"}
