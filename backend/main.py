from dotenv import load_dotenv
import os
load_dotenv()

from fastapi import FastAPI, WebSocket
from backend.routes import waittimes
from backend.whisper_transcriber import transcribe_audio
from backend.gpt_assistant import ask_gpt
from backend.auth import get_current_user
from backend.logs import log_error
import tempfile

app = FastAPI()

app.include_router(waittimes.router, prefix="/api/waittimes")

@app.websocket("/ws/transcribe")
async def websocket_transcribe(websocket: WebSocket):
    await websocket.accept()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        while True:
            try:
                data = await websocket.receive_bytes()
                temp_audio.write(data)
                temp_audio.flush()
                text = transcribe_audio(temp_audio.name)
                await websocket.send_text(text)
            except Exception as ex:
                log_error(str(ex), origin="WebSocket")
                await websocket.send_text("[WebSocket-feil] " + str(ex))
