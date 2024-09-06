from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from model import RootModel
from config import API_TOKEN

app = FastAPI()

# Определите список разрешенных источников (origin), методов, заголовков и др.
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Referertelegram"],
)

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Неверный токен аутентификации")
    return credentials.credentials

@app.post("/api/data")
async def validate_data(data: RootModel, token: str = Depends(verify_token)):
    return {"success": True, "data": data, "error": None}

