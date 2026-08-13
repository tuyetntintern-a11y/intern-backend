from sqladmin import Admin, ModelView

from app.models import Author, Book, Category


class AuthorAdmin(ModelView, model=Author):
    column_list = [
        Author.id,
        Author.name,
        Author.bio,
        Author.country,
        Author.birth_year,
    ]
    name = "Author"
    name_plural = "Authors"


class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.title, Book.year, Book.summary, Book.author_id]
    name = "Book"
    name_plural = "Books"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    name = "Category"
    name_plural = "Categories"


def setup_admin(app, engine):
    admin = Admin(app, engine, title="Books Admin")
    admin.add_view(AuthorAdmin)
    admin.add_view(BookAdmin)
    admin.add_view(CategoryAdmin)
    
    return admin
# SQLAdmin  → quản lý dữ liệu, Có thể xem, thêm, sửa và xóa qua giao diện: http://127.0.0.1:8000/admin
# Alembic   → quản lý cấu trúc database(Thêm cột, Xóa cột, Đổi kiểu dữ liệu, Tạo khóa ngoại mới,...)
# Model     → mô tả bảng mong muốn
# create_all → tạo bảng mới lần đầu(Tạo bảng chưa tồn tại.)