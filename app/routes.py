from fastapi import APIRouter, HTTPException

from app.database import redis_client
from app.schemas import Data, WriteResponseSchema, CheckResponseSchema


router = APIRouter()


@router.post("/write_data", response_model=WriteResponseSchema)
async def write_data(data: Data):
    """ Записать/обновить данные
    Пример тела запроса:
        {
            "phone": "89323234912",
            "address": "текстовый адрес"
        }
    """
    redis_client.set(data.phone, data.address)
    return {"status": "success"}


@router.get("/check_data", response_model=CheckResponseSchema)
async def check_data(phone: str):
    """ Запрос на получение данных
    Query params:
        phone: str - номер телефона
    """
    address = redis_client.get(phone)
    if address is None:
        raise HTTPException(status_code=404, detail="Phone not found")
    return {"address": address}
