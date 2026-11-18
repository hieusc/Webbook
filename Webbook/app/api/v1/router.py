from fastapi import APIRouter
from api.v1.endpoints import book, user

api_router = APIRouter()
api_router.include_router(book.router, prefix="/books", tags=["Books"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
