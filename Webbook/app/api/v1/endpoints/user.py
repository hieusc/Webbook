from typing import List
from fastapi import APIRouter, Depends, status

from db.base import get_db
from schemas.user import UserCreate, UserOut
from services import users as s

router = APIRouter()


@router.get("/", response_model=List[UserOut])
def get_all_user(cur=Depends(get_db)):
    return s.get_all_user(cur)


# Các route có đường dẫn cố định (/phone, /email) phải đặt TRƯỚC /{id}
@router.get("/phone/{phone}", response_model=UserOut)
def get_phone_user(phone: str, cur=Depends(get_db)):
    return s.get_phone_user(cur, phone)


@router.get("/email/{email}", response_model=UserOut)
def get_email_user(email: str, cur=Depends(get_db)):
    return s.get_email_user(cur, email)


@router.get("/{id}", response_model=UserOut)
def get_id_user(id: int, cur=Depends(get_db)):
    return s.get_id_user(cur, id)


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(data_user: UserCreate, cur=Depends(get_db)):
    return s.create_user(cur, data_user)


@router.put("/{id}", response_model=UserOut)
def update_user(id: int, data_user: UserCreate, cur=Depends(get_db)):
    return s.update_user(cur, id, data_user)


@router.delete("/{id}")
def delete_user(id: int, cur=Depends(get_db)):
    return s.delete_user(cur, id)
