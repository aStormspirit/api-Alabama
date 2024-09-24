from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from model import RootModel
from config import API_TOKEN
from utils import run_docker_container
from celery.result import AsyncResult
import json
import uuid


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

def create_json_file(data: RootModel):
    # Генерируем уникальный идентификатор для имени файла
    id_name = str(uuid.uuid4())
    name = f'./data/{id_name}.json'
    
    # Сохраняем объект data в формате JSON с уникальным именем файла
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(data.dict(), f, ensure_ascii=False, indent=4)
    
    return id_name


@app.post("/api/data")
async def validate_data(data: RootModel, token: str = Depends(verify_token)):    
    id_name = create_json_file(data)
    task = run_docker_container.delay("test")
    return {"message": "Задача создана и выполняется в фоновом режиме", "task_id": task.id}

@app.get("/api/result/{task_id}")
async def get_result(task_id: str, token: str = Depends(verify_token)):
    task_result = AsyncResult(task_id)
    if task_result.ready():
        result = task_result.get()
        print(result)
        if "1 passed" in result:
            return {"status": "COMPLETED", "result": {"success": True, "error": None}}
        else:
            return {"status": "COMPLETED", "result": {"success": False, "error": "Test failed"}}
    else:
        return {"status": "PENDING", "result": None}

