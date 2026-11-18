from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    """Dữ liệu gửi lên khi thêm / sửa sách."""
    name: str = Field(min_length=1)
    author: str
    price: float = Field(ge=0)      # không cho giá âm
    soluong: int = Field(ge=0)      # không cho số lượng âm
    type: str


class BookOut(BookCreate):
    """Dữ liệu trả về: có thêm id."""
    id: int
