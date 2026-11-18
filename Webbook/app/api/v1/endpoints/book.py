from typing import List
from fastapi import APIRouter, Depends, status

from db.base import get_db
from schemas.book import BookCreate, BookOut
from services import books as b

router = APIRouter()


@router.get("/", response_model=List[BookOut])
def get_all_books(cur=Depends(get_db)):
    return b.get_all_books(cur)


@router.get("/{id}", response_model=BookOut)
def get_book(id: int, cur=Depends(get_db)):
    return b.get_book_by_id(cur, id)


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, cur=Depends(get_db)):
    return b.create_book(cur, book)


@router.put("/{id}", response_model=BookOut)
def update_book(id: int, book: BookCreate, cur=Depends(get_db)):
    return b.update_book(cur, id, book)


@router.delete("/{id}")
def delete_book(id: int, cur=Depends(get_db)):
    return b.delete_book(cur, id)
