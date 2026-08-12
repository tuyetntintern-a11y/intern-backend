from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)# khóa chính
    name: Mapped[str] = mapped_column(String(200), nullable=False)# (tên tác giả)
    bio: Mapped[str] = mapped_column(String(1000), nullable=True)# (tiểu sử)
    country: Mapped[str] = mapped_column(String(100), nullable=True)# (quốc gia)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=True)# (năm sinh)
