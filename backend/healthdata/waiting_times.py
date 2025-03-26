
import json
from difflib import get_close_matches

with open("data/treatments_waiting.json", "r", encoding="utf-8") as f:
    WAIT_DATA = json.load(f)

def get_waiting_time(treatment: str, location: str = None):
    treatment = treatment.lower().replace(" ", "_")
    match = get_close_matches(treatment, WAIT_DATA.keys(), n=1, cutoff=0.5)

    if not match:
        return {"error": "Fant ikke behandlingstype."}

    selected = match[0]
    hospitals = WAIT_DATA[selected]

    if location:
        best_match = get_close_matches(location, hospitals.keys(), n=1, cutoff=0.4)
        if best_match:
            return { "treatment": selected, "location": best_match[0], "wait": hospitals[best_match[0]] }

    return { "treatment": selected, "all_locations": hospitals }
