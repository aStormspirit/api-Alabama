from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from model import RootModel, StateEnum
from config import API_TOKEN
import subprocess
import os


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

@app.post("/api/run_docker")
async def run_docker(token: str = Depends(verify_token)):
    try:
        # Запуск Docker контейнера
        subprocess.run(['docker', 'run', '-d', 'kansas-script'], check=True)
        return {"success": True, "message": "Docker контейнер успешно запущен"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при запуске Docker контейнера: {str(e)}")


def start_script(state: StateEnum):
        # Запуск скрипта Alabama
    script_path = os.path.join('scripts', f'{state.value}.py')
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при выполнении скрипта: {str(e)}")

@app.post("/api/data")
async def validate_data(data: RootModel, token: str = Depends(verify_token)):
    start_script(data.state)
    return {"success": True, "data": data, "error": None}

