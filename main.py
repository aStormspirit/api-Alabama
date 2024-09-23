from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from model import RootModel
from config import API_TOKEN
from utils import run_and_wait_for_container
from celery.result import AsyncResult

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


# def process_data(data: RootModel):вщс
#     result = run_and_wait_for_container("kansas")
#     if "1 passed" in result:
#         return {"success": True, "data": data, "error": None}
#     else:
#         return {"success": False, "data": data, "error": "Test failed"}

@app.post("/api/data")
async def validate_data(data: RootModel, token: str = Depends(verify_token)):
    task = run_and_wait_for_container.delay("kansas")
    return {"message": "Задача создана и выполняется в фоновом режиме", "task_id": task.id}

@app.get("/api/result/{task_id}")
async def get_result(task_id: str, token: str = Depends(verify_token)):
    task_result = AsyncResult(task_id)
    if task_result.ready():
        result = task_result.get()
        if "1 passed" in result[0]:
            return {"status": "COMPLETED", "result": {"success": True, "error": None}}
        else:
            return {"status": "COMPLETED", "result": {"success": False, "error": "Test failed"}}
    else:
        return {"status": "PENDING", "result": None}

