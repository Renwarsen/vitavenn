
# 📘 Vitavenn v11.4

Stemmestyrt og strategisk AI-verktøy for helseledere i Norge. Denne versjonen er fullstendig klar for lokal utvikling og deploy via Render.

---

## 🚀 Komme i gang

### 📦 Installer avhengigheter

Backend (Python):
```bash
cd vitavenn_v11.3_complete_260325
pip install -r requirements.txt
```

Frontend (React):
```bash
cd frontend
npm install
npm run dev
```

---

## 🛠 Miljøvariabler

Opprett `backend/.env` med følgende (eksempel):

```
OPENAI_API_KEY=din-openai-nøkkel
CRIIPTO_DOMAIN=vitavenn-test.criipto.id
CRIIPTO_CLIENT_ID=ditt-criipto-id
JWT_SECRET=hemmeligjwt
BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
```

---

## ▶️ Kjøre lokalt

```bash
bash start.sh
```

Eller manuelt:
```bash
cd backend
uvicorn main:app --reload
```

---

## 🌐 API-endepunkter

| Endpoint | Beskrivelse |
|----------|-------------|
| `/api/waittimes` | Ventetidssøk |
| `/ws/transcribe` | WebSocket for sanntids transkripsjon |
| `/auth` | (krever Criipto-integrasjon) |

---

## ☁️ Deploy til Render

1. Push til GitHub
2. Opprett Render Web Service:
   - Python 3.x
   - Start kommando: `uvicorn backend.main:app --host=0.0.0.0 --port=10000`
3. Legg inn samme miljøvariabler som i `.env`

---

## 🧪 Testing

- API: Postman / curl
- Transkripsjon: send dummy-lydfil via WebSocket
- Frontend: `npm run dev` og test søk + stemmebruk

---

## 🔐 Sikkerhet

- JWT med Criipto
- `.env` er ignorert med `.gitignore`
- Automatisk fallback ved lav API-konfidens

---

## 📄 Struktur

- `backend/` – FastAPI + AI-moduler
- `frontend/` – React-komponenter (stemmestyrt søk)
- `data/` – Ventetidsdata
