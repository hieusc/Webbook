from fastapi import HTTPException
from crud import user as u


def get_all_user(cur):
    return u.get_all_user(cur)


def get_id_user(cur, id: int):
    user = u.get_id_user(cur, id)
    if not user:
        raise HTTPException(status_code=404, detail="Id khong ton tai")
    return user


def get_email_user(cur, email: str):
    user = u.get_email_user(cur, email)
    if not user:
        raise HTTPException(status_code=404, detail="Email khong ton tai")
    return user


def get_phone_user(cur, phone: str):
    user = u.get_phone_user(cur, phone)
    if not user:
        raise HTTPException(status_code=404, detail="Phone khong ton tai")
    return user


def _check_trung(cur, data_user, id_hien_tai: int | None = None):
    for found in (u.get_email_user(cur, data_user.email), u.get_phone_user(cur, data_user.phone)):
        if found and found["id"] != id_hien_tai:
            raise HTTPException(status_code=409, detail="Email hoac phone da ton tai")


def create_user(cur, data_user):
    _check_trung(cur, data_user)
    return u.create_user(cur, data_user)


def update_user(cur, id: int, data_user):
    get_id_user(cur, id)  
    _check_trung(cur, data_user, id_hien_tai=id)
    return u.update_user(cur, id, data_user)


def delete_user(cur, id: int):
    get_id_user(cur, id)
    u.delete_user(cur, id)
    return {"message": "Xoa thanh cong"}
