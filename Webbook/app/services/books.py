from fastapi import HTTPException
from crud import book


def get_all_books(cur):
    return book.get_all_books(cur)


def get_book_by_id(cur, id: int):
    data = book.get_book_by_id(cur, id)
    if not data:
        raise HTTPException(status_code=404, detail="Id sach khong ton tai")
    return data


def create_book(cur, book_data):
    if book.get_book_by_name(cur, book_data.name):
        raise HTTPException(status_code=409, detail="Ten sach da ton tai")
    return book.create_book(cur, book_data)


def update_book(cur, id: int, book_data):
    get_book_by_id(cur, id)  # tự báo 404 nếu không có

    # Không cho đổi tên trùng với một cuốn sách KHÁC
    same_name = book.get_book_by_name(cur, book_data.name)
    if same_name and same_name["id"] != id:
        raise HTTPException(status_code=409, detail="Ten sach da ton tai")

    return book.update_book(cur, id, book_data)


def delete_book(cur, id: int):
    get_book_by_id(cur, id)
    book.delete_book(cur, id)
    return {"message": "Xoa thanh cong"}
