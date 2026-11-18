from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """Dữ liệu gửi lên khi thêm / sửa user."""
    name: str = Field(min_length=1)
    age: int = Field(ge=0)
    phone: str
    email: str


class UserOut(UserCreate):
    """Dữ liệu trả về: có thêm id, KHÔNG có mật khẩu (mk)."""
    id: int
