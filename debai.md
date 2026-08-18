# Hướng dẫn JWT — Week 3

Sample tuần 3 **đã có API Book CRUD**. Tuần này làm thêm: CRUD User, login JWT, gắn token khi ghi sách (chỉ admin được xóa), rồi clone front-end có sẵn để kiểm tra API.

GET Book và GET User không cần token. POST/PUT Book cần login. DELETE Book, PUT/DELETE User cần login quyền admin (`role === 0`).

Mỗi bài xong → **1 commit** trên nhánh `week3/fastapi-jwt-auth`.


| Bài | Message                         |
| --- | ------------------------------- |
| 1   | `bai1: confirm sample layout`   |
| 2   | `bai2: users crud`              |
| 3   | `bai3: jwt login`               |
| 4   | `bai4: protect book write apis` |
| 5   | `bai5: connect frontend`        |


---

## Mục lục

1. [Hai khái niệm cần nhớ](#1-hai-khái-niệm-cần-nhớ)
2. [Chuẩn bị](#2-chuẩn-bị)
3. [Bài 1 — Chạy sample](#bài-1--chạy-sample)
4. [Bài 2 — User CRUD](#bài-2--user-crud)
5. [Bài 3 — Login trả JWT](#bài-3--login-trả-jwt)
6. [Bài 4 — Gắn token vào API ghi](#bài-4--gắn-token-vào-api-ghi)
7. [Bài 5 — Chạy front-end](#bài-5--chạy-front-end)
8. [Checklist](#checklist)
9. [Lỗi thường gặp](#lỗi-thường-gặp)

---

## 1. Hai khái niệm cần nhớ

**Authentication:** login đúng username/password thì server biết đó là user nào.

**Authorization:** user đó được làm gì. `role` là số: `0` **= admin**, **khác 0 = user** (mặc định `1`). Ai đã login (user hoặc admin) đều tạo và sửa sách được. Chỉ admin xóa sách và sửa/xóa user.


| Mã      | Nghĩa                                            |
| ------- | ------------------------------------------------ |
| **401** | Chưa login, token sai, hoặc hết hạn              |
| **403** | Đã login nhưng `role != 0` (ví dụ user xóa sách) |


Gửi token bằng header (có **một dấu cách** sau `Bearer`):

```text
Authorization: Bearer <chuỗi_token>
```

Mật khẩu lưu cột `hashed_password` (bcrypt) **trên server**. JSON gửi lên lúc tạo user / login là password lúc gõ, ví dụ `"secret123"`. FastAPI hash khi lưu, so khớp khi login. Front-end Vue cũng gửi nguyên văn — không hash trên trình duyệt.

---

## 2. Chuẩn bị

- Python 3.11+, Git, VS Code / Cursor
- Postman hoặc REST Client — dùng để gọi API (không bắt buộc lưu file `.http`)
- Node.js 18+ (bài 5)
- Đã hiểu tuần 2: router, service, schema, `Depends(get_db)`

```bash
git checkout -b week3/fastapi-jwt-auth
```

Tải folder `week3/sample` → **copy toàn bộ file bên trong** vào repo (nhánh vừa tạo).

```bash
python -m venv venv
```

Kích hoạt `venv`, rồi:

```bash
pip install -r requirements.txt
cp .env.example .env
```

Windows CMD: `copy .env.example .env`

```bash
uvicorn app.main:app --reload
```

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

File `.env` đã có trong `.gitignore`. Bài 3 thêm `SECRET_KEY` vào `.env` — không commit file này.

### Status code


| Tình huống                                       | Status            |
| ------------------------------------------------ | ----------------- |
| GET Book / GET User, không token                 | **200**           |
| Body sai khuôn (Pydantic)                        | **422**           |
| Username trùng lúc POST / PUT User               | **409**           |
| Sai username/password lúc login                  | **401**           |
| POST/PUT/DELETE Book thiếu hoặc sai token        | **401**           |
| PUT/DELETE User thiếu hoặc sai token             | **401**           |
| Tạo / sửa Book có token đúng                     | **201** / **200** |
| `role != 0` gọi DELETE Book hoặc PUT/DELETE User | **403**           |
| Admin xóa Book hoặc User                         | **204**           |
| Book id / User id không có                       | **404**           |


---

## Bài 1 — Chạy sample

### Mục tiêu

Chạy được Book CRUD. Biết `books.py` là file bài 4 sẽ gắn token.

### Việc cần làm

Đọc:

- `app/main.py` — Hello, `include_router` Book
- `app/api/routers/books.py` — GET/POST/PUT/DELETE (bài 4 mới gắn token)
- `app/core/config.py` — `Settings`, `get_settings()` (bài 3 thêm field JWT)
- `.env.example`

Chạy `uvicorn`. Mở `/docs`. Gọi `GET /api/v1/books`. POST một quyển sách (sample chưa bắt token → 201).

### Tự kiểm

- [ ] `GET /` ra Hello
- [ ] `GET /api/v1/books` ra list
- [ ] Biết `books.py` là chỗ gắn `Depends` ở bài 4

```bash
git add .
git commit -m "bai1: confirm sample layout"
```

---

## Bài 2 — User CRUD

### Mục tiêu

Bảng `users`. CRUD API giống các bài trước.


| Method | Path                      | Status                      |
| ------ | ------------------------- | --------------------------- |
| POST   | `/api/v1/users`           | **201**                     |
| GET    | `/api/v1/users`           | **200**                     |
| GET    | `/api/v1/users/{user_id}` | **200** / **404**           |
| PUT    | `/api/v1/users/{user_id}` | **200** / **404** / **409** |
| DELETE | `/api/v1/users/{user_id}` | **204** / **404**           |


Bài này các API đều gọi được không cần login. Bài 4 mới khóa PUT/DELETE chỉ quyền admin. POST `/users` luôn mở để có thể tạo tài khoản mới.

`role`: số nguyên. `0` = admin; khác `0` = user. Thiếu field thì mặc định `1`.

### 1) Model — `app/models/user.py`

```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # TODO: username — String(50), unique=True, index=True, nullable=False
    # TODO: hashed_password — String(255), nullable=False
    # TODO: role — Integer, nullable=False, default=1
```

Sửa `app/models/__init__.py` (giữ `Book`, thêm `User`):

```python
from app.models.book import Book
from app.models.user import User

__all__ = ["Book", "User"]
```

### 2) Tạo bảng `users` bằng Alembic

Không cần tắt `uvicorn`. `--reload` tự chạy lại khi lưu file Python. `upgrade` chỉ sửa DB — request sau là dùng bảng mới.

Sample đã tạo `books` bằng `create_all`, chưa có lịch sử Alembic. Khớp Alembic với DB hiện tại **trước** khi thêm User (`env.py` lúc này vẫn chỉ `Book`):

```python
from app.models import Book  # noqa: F401
```

```bash
alembic revision --autogenerate -m "baseline"
alembic stamp head
```

`stamp` vì `books` đã có. `upgrade` bước này sẽ lỗi `table already exists`.

Import `User` trong `alembic/env.py`:

```python
from app.models import Book, User  # noqa: F401
```

```bash
alembic revision --autogenerate -m "add users"
alembic upgrade head
```

File mới trong `alembic/versions/` phải có `op.create_table("users", ...)`.

Nếu Alembic báo `database is locked` (Windows, uvicorn đang giữ file `.db`): dừng uvicorn, chạy lại hai lệnh `upgrade`/`stamp`, rồi `uvicorn app.main:app --reload`.

### 3) Hash mật khẩu — `app/core/security.py`

```python
import bcrypt


def hash_password(plain: str) -> str:
    # TODO: bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    ...


def verify_password(plain: str, hashed: str) -> bool:
    # TODO: bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
    ...
```

`hashpw` nhận `bytes`. Lưu DB thì `.decode("utf-8")` thành `str`.

Body POST `/users` và POST `/auth/login` gửi password **chưa hash**. `hash_password` chỉ gọi trong `create_user` (và PUT nếu đổi password). Login dùng `verify_password(plain, hashed)` — so chuỗi người dùng gõ với hash trong DB.

### 4) Schema — `app/schemas/user.py`

```python
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=100)
    role: int = 1


class UserRead(BaseModel):
    id: int
    username: str
    role: int
    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str | None = Field(default=None, min_length=8, max_length=100)
    role: int = 1
```

`UserRead`: `id`, `username`, `role`. `role` không phải số → **422**. Số `2`, `99`, … vẫn 201, coi như quyền user.

PUT: username + role bắt buộc. Không gửi `password` → giữ pass cũ. Có gửi → lưu pass mới đã mã hóa lại.

### 5) Service — `app/services/user_service.py`

```python
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models import User
from app.schemas.user import UserCreate, UserUpdate


def get_user_by_username(db: Session, username: str) -> User | None:
    # TODO: select User where username == ... ; return scalar hoặc None
    ...


def get_user(db: Session, user_id: int) -> User:
    # TODO: db.get(User, user_id); None → HTTPException 404 "User not found"
    ...


def list_users(db: Session) -> list[User]:
    # TODO: select User order_by id; return list(db.scalars(stmt))
    ...


def create_user(db: Session, payload: UserCreate) -> User:
    # TODO: nếu get_user_by_username khác None → HTTPException 409 "Username already exists"
    # TODO: User(username=..., hashed_password=hash_password(payload.password), role=payload.role)
    # TODO: add, commit, refresh, return
    ...


def update_user(db: Session, user_id: int, payload: UserUpdate) -> User:
    # TODO: user = get_user(...)
    # TODO: username mới trùng user khác (id khác) → 409
    # TODO: user.username = payload.username; user.role = payload.role
    # TODO: nếu payload.password is not None → hashed_password = hash_password(...)
    # TODO: commit, refresh, return
    ...


def delete_user(db: Session, user_id: int) -> None:
    # TODO: user = get_user(...); db.delete(user); commit
    ...
```

Password quá ngắn lúc POST → **422**. Username trùng → **409**. Id không có → **404**.

### 6) Router — `app/api/routers/users.py`

Giống `books.py`:

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services import user_service

router = APIRouter(tags=["users"])


@router.post("/users", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    return user_service.create_user(db, payload)


@router.get("/users", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)) -> list[UserRead]:
    return user_service.list_users(db)


@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    return user_service.get_user(db, user_id)


@router.put("/users/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
) -> UserRead:
    return user_service.update_user(db, user_id, payload)


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> None:
    user_service.delete_user(db, user_id)
```

`app/main.py`: import `User`, `include_router(users.router, prefix="/api/v1")` cạnh Book.

### Tự kiểm

Gọi API bằng Postman hoặc REST Client.

```json
{
  "username": "minh",
  "password": "secret123",
  "role": 1
}
```

Thiếu `role` → mặc định `1`. Admin: `"role": 0`.

- [ ] POST → **201**, body có `id`, `username`, `role`; không có `password` / `hashed_password`
- [ ] Cùng username lần 2 → **409**
- [ ] `"password": "123"` → **422**
- [ ] `"role": "admin"` (chuỗi) → **422**
- [ ] `"role": 2` → 201 (user; xóa sách bài 4 sẽ 403)
- [ ] `GET /api/v1/users` → list, không có hash
- [ ] `GET /api/v1/users/{id}` đúng → 200; id sai → **404**
- [ ] PUT username + `role`, không gửi password → 200; login vẫn password cũ
- [ ] PUT username trùng user khác → **409**
- [ ] DELETE → **204**; GET lại id đó → **404**
- [ ] Mở `data/books.db`: cột `hashed_password` không phải `secret123` (`/admin` sample chỉ có Book)

**Backlog:** chụp **1 ảnh** POST `/api/v1/users` **201** và **1 ảnh** GET `/users` → gửi lên Backlog.

```bash
git add .
git commit -m "bai2: users crud"
```

---

## Bài 3 — Login trả JWT

### Mục tiêu

`POST /api/v1/auth/login` nhận JSON. Đúng → token. Sai → **401**.

Body:

```json
{
  "username": "minh",
  "password": "secret123"
}
```

Header: `Content-Type: application/json`. `password` trong body là chuỗi lúc gõ, cùng lúc tạo user — không gửi hash.

Response:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

JWT có ba khúc cách nhau bởi dấu chấm: header, payload (`sub` = username, `exp` = hết hạn), signature. Server ký bằng `secret_key`.

### 1) Settings — sửa `app/core/config.py` và `.env`

Sample mới có `app_title` và `database_url`. Thêm ba field JWT:

```python
class Settings(BaseSettings):
    app_title: str = "Books API"
    database_url: str | None = None
    # TODO: secret_key — str (chuỗi ký JWT)
    # TODO: jwt_algorithm — str, mặc định "HS256"
    # TODO: access_token_expire_minutes — int, mặc định 30

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
```

Pydantic đọc `.env`: tên biến viết HOA, trong code viết thường (`SECRET_KEY` → `settings.secret_key`).

Sửa `.env.example` và file `.env` (copy từ `.env.example` nếu chưa có):

```text
# TODO: SECRET_KEY=...  (chuỗi dài, khó đoán; đừng commit .env)
# TODO: ACCESS_TOKEN_EXPIRE_MINUTES=30
```

`jwt_algorithm` để mặc định `"HS256"` trong `config.py` là đủ, không bắt buộc ghi trong `.env`.

Đổi `.env` rồi **restart uvicorn**.

### 2) Schema — thêm vào `app/schemas/user.py`

```python
class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

### 3) Tạo token — sửa `app/core/security.py`

```python
from datetime import datetime, timedelta, timezone

import jwt

from app.core.config import get_settings


def create_access_token(subject: str) -> str:
    settings = get_settings()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    # TODO: payload = {"sub": subject, "exp": expire}
    # TODO: jwt.encode(..., settings.secret_key, algorithm=settings.jwt_algorithm)
    ...
```

`sub` = username (chuỗi). `exp` bắt buộc — lấy từ `settings.access_token_expire_minutes`.

### 4) Service login — sửa `user_service.py`

```python
from app.core.security import create_access_token, verify_password


def login(db: Session, username: str, password: str) -> str:
    user = get_user_by_username(db, username)
    # TODO: nếu user is None hoặc verify_password sai
    #       → HTTPException 401 "Incorrect username or password"
    # TODO: return create_access_token(user.username)
    ...
```

Sai user và sai password cùng một câu 401 (tránh để người khác dò username nào tồn tại).

### 5) Router — tạo `app/api/routers/auth.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import LoginRequest, Token
from app.services import user_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> Token:
    # TODO: token = user_service.login(db, payload.username, payload.password)
    # TODO: return Token(access_token=token)
    ...
```

`include_router(auth.router, prefix="/api/v1")` → `POST /api/v1/auth/login`.

### Tự kiểm

- [ ] POST `/users` rồi login đúng → 200, có `access_token`, `token_type` là `"bearer"`
- [ ] Password sai → **401**
- [ ] Username không có → **401** (cùng message)

**Backlog:** chụp **1 ảnh** login **200** (che bớt token nếu gửi public) → gửi lên Backlog.

```bash
git add .
git commit -m "bai3: jwt login"
```

---

## Bài 4 — Gắn token vào API ghi

### Mục tiêu


| API                                  | Ai gọi được                                    |
| ------------------------------------ | ---------------------------------------------- |
| GET Book, GET User, POST User, login | Không cần token                                |
| POST / PUT Book, GET `/auth/me`      | Đã login (`get_current_user`)                  |
| DELETE Book, PUT / DELETE User       | Đã login và `role === 0` (`get_current_admin`) |


Thiếu / sai token lúc ghi → **401**. Login với quyền user xóa sách / sửa user →  Trả lỗi **403**. Login quyền admin xóa → Thành công **204**.

`Depends` chạy trước hàm service. Quyền đọc `role` trên **DB**.

### 1) `app/api/deps.py`

Để `get_current_user` ở `deps.py` (không để trong `security.py` — file đó đã bị `user_service` import, dễ vòng import).

Dùng `OAuth2PasswordBearer` như trên slide: đọc header `Authorization: Bearer ...`.

```python
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.db.session import get_db
from app.models import User
from app.services.user_service import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    settings = get_settings()
    try:
        # TODO: jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        # TODO: username = payload.get("sub"); nếu None → raise credentials_exception
        ...
    except InvalidTokenError:
        raise credentials_exception

    # TODO: user = get_user_by_username(...); nếu None → raise credentials_exception
    # TODO: return user
    ...


def get_current_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    # TODO: current_user.role != 0 → HTTPException 403 "Not enough permissions"
    # TODO: return current_user
    ...
```

`tokenUrl` chỉ để `/docs` biết chỗ login. Login nhận **JSON**; nút Authorize trên Swagger hay gửi **form** → dễ lệch. Test bằng Postman hoặc REST Client.

Thiếu header: `OAuth2PasswordBearer` tự trả 401.

### 2) `GET /api/v1/auth/me`

Trả user đang login (có `role`). Front-end dùng để ẩn nút Xóa.

Trong `auth.py` (thêm import `User`, `UserRead`):

```python
from app.api.deps import get_current_user
from app.models import User
from app.schemas.user import LoginRequest, Token, UserRead


@router.get("/me", response_model=UserRead)
def read_me(current_user: User = Depends(get_current_user)) -> UserRead:
    return current_user
```

### 3) Router Book

POST / PUT: `get_current_user`. DELETE: `get_current_admin`. GET giữ `Depends(get_db)`.

```python
from app.api.deps import get_current_admin, get_current_user
from app.models import User


@router.post("/books", response_model=BookRead, status_code=201)
def create_book(
    payload: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BookRead:
    return book_service.create_book(db, payload)


@router.put("/books/{book_id}", response_model=BookRead)
def update_book(
    book_id: int,
    payload: BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BookRead:
    return book_service.update_book(db, book_id, payload)


@router.delete("/books/{book_id}", status_code=204)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> None:
    book_service.delete_book(db, book_id)
```

Thân hàm không dùng `current_user` vì bài này không lưu “ai tạo sách”. Tham số đó chỉ để FastAPI **chạy `Depends` trước khi vào hàm**: có token hợp lệ mới tới `book_service`. Thiếu `Depends` thì không đọc token (không 401) và không kiểm tra `role` (không 403).

### 4) Router User

PUT / DELETE: `get_current_admin`. GET và POST giữ như bài 2.

```python
from app.api.deps import get_current_admin
from app.models import User


@router.put("/users/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> UserRead:
    return user_service.update_user(db, user_id, payload)


@router.delete("/users/{user_id}", status_code=204)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
) -> None:
    user_service.delete_user(db, user_id)
```

### Tự kiểm

Tạo hai account: `role: 1` và `role: 0`.

- [ ] `GET /api/v1/books` không header → **200**
- [ ] `POST /api/v1/books` không header → **401**
- [ ] Token user: POST Book → **201**; PUT → **200**; DELETE → **403** (sách còn)
- [ ] Token admin: DELETE Book → **204**
- [ ] DELETE Book không token → **401**
- [ ] `GET /api/v1/users` không token → **200**
- [ ] PUT / DELETE user: không token → **401**; `role != 0` → **403**; admin → 200 / 204
- [ ] Token sửa 1 ký tự → **401**
- [ ] `GET /api/v1/auth/me` (Bearer) → có `role`

**Backlog:** chụp **1 ảnh** POST Book **401**, **1 ảnh** POST **201**, **1 ảnh** DELETE **403** → gửi lên Backlog.

```bash
git add .
git commit -m "bai4: protect book write apis"
```

---

## Bài 5 — Chạy front-end

### Mục tiêu

Điền CORS cho cổng Vite, clone front-end, `npm run dev`, kiểm tra JWT + `role` với API đang chạy.

### 1) CORS — sửa `app/main.py`

**CORS** (Cross-Origin Resource Sharing) là luật của **trình duyệt**, không phải của FastAPI hay Postman.

Một **origin** = `scheme://host:port`. Khác **một** trong ba phần là origin khác. Front-end Vite `http://localhost:5173` và API `http://127.0.0.1:8000` khác cả host lẫn cổng → trình duyệt **chặn** JS trên trang 5173 gọi API 8000, trừ khi server nói “origin này được phép”.

`localhost` và `127.0.0.1` cũng là hai origin khác nhau, dù cùng máy. Mở front-end bằng URL nào thì `allow_origins` phải có origin đó.

FastAPI dùng `CORSMiddleware`: list trong `allow_origins` được gửi ra header `Access-Control-Allow-Origin`. Thiếu origin của trang front-end → DevTools console kiểu `blocked by CORS policy`, front-end báo lỗi dù uvicorn vẫn chạy và Postman vẫn 200 (Postman / REST Client không đi qua luật CORS của browser).

Sample để TODO. Điền origin Vite (`npm run dev`):

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # TODO: origin Vite `npm run dev` — localhost
        # TODO: origin Vite `npm run dev` — 127.0.0.1
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Hai chuỗi cần thêm: `"http://localhost:5173"` và `"http://127.0.0.1:5173"`. Sửa xong **restart uvicorn** nếu `--reload` chưa bắt.

### 2) Clone và chạy front-end

Clone front-end ra folder riêng, cạnh repo API. Cần Node.js 18+. Hai terminal: `uvicorn` cổng 8000 và `npm run dev` cổng 5173.

```bash
git clone https://github.com/Phongnx-vnext/intern202607_week3_frontend.git
cd intern202607_week3_frontend
npm install
npm run dev
```

Mở [http://localhost:5173](http://localhost:5173).

API mặc định: `http://127.0.0.1:8000/api/v1`. Cần đổi thì tạo `.env` trong folder vừa clone rồi **restart** `npm run dev`:

```text
VITE_API_URL=http://127.0.0.1:8000/api/v1
```

### Tự kiểm trên front-end

- [ ] CORS 5173 đã điền thì front-end gọi được API
- [ ] Chưa login: thấy danh sách sách
- [ ] Tạo user `role: 1` → login → thêm / sửa sách; không có nút Xóa
- [ ] Tạo user `role: 0` → login → có nút Xóa, xóa được

**Backlog:** chụp **1 ảnh** front-end user (không nút Xóa) và **1 ảnh** front-end admin (có nút Xóa) → gửi lên Backlog.

```bash
git add .
git commit -m "bai5: connect frontend"
```

---

## Checklist

- [ ] `git log` có `bai1` … `bai5`
- [ ] `POST /api/v1/users` → 201; trùng username → 409; `role` không phải số → 422
- [ ] GET / PUT / DELETE `/users` đúng status
- [ ] Password trong DB là hash
- [ ] `POST /api/v1/auth/login` JSON → `access_token`
- [ ] Sai login → 401
- [ ] GET Book / GET User không token → 200
- [ ] POST/PUT Book không token → 401; có token → 201 / 200
- [ ] DELETE Book: không token → 401; `role != 0` → **403**; admin → **204**
- [ ] PUT/DELETE User: không token → 401; `role != 0` → **403**; admin → 200 / 204
- [ ] User `role: 0` xóa được sách
- [ ] Front-end bài 5: user không thấy nút Xóa; admin xóa được
- [ ] `.env` không nằm trên GitHub

---

## Lỗi thường gặp


| Lỗi                                             | Nguyên nhân                                                | Cách xử lý                                                    |
| ----------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------- |
| POST Book vẫn 201 khi không token               | Chưa `Depends(get_current_user)` trên create               | Gắn POST/PUT Book; DELETE Book dùng `get_current_admin`       |
| PUT User vẫn 200 khi không token                | Chưa `Depends(get_current_admin)`                          | Gắn PUT/DELETE `/users`                                       |
| GET Book / GET User ra 401                      | Gắn Depends lên cả router                                  | GET chỉ `Depends(get_db)`                                     |
| `"role": "admin"` ra 201                        | `role` phải là `int`                                       | Pydantic → 422                                                |
| User xóa sách ra 204                            | DELETE còn `get_current_user` hoặc so sánh chuỗi `"admin"` | `role != 0` → 403                                             |
| User xóa sách ra 401                            | Token không gửi / hết hạn                                  | 401 = chưa xác thực; 403 = sai quyền                          |
| `Invalid header`                                | Thiếu `Bearer` (có space)                                  | `Authorization: Bearer eyJ...`                                |
| Login 422                                       | Gửi form, API nhận JSON                                    | `Content-Type: application/json`                              |
| `Could not validate credentials` ngay sau login | Sai `SECRET_KEY` lúc encode/decode, hoặc copy thiếu token  | Một `.env`; copy nguyên `access_token`                        |
| POST user 201 nhưng login 401                   | Lưu password thô / verify sai bytes                        | `hash_password` lúc create; `verify_password` lúc login       |
| Hash hiện trên `/docs`                          | `UserRead` còn field password                              | `id`, `username`, `role`                                      |
| Swagger Authorize login fail                    | Swagger gửi form                                           | Postman hoặc REST Client, body JSON                           |
| Token hết hạn nhanh                             | `ACCESS_TOKEN_EXPIRE_MINUTES` nhỏ                          | Tăng trong `.env`, restart uvicorn                            |
| Front-end không gọi được API                    | CORS chưa điền 5173, hoặc API không chạy cổng 8000         | Điền origin bài 5; restart uvicorn                            |
| Đổi `VITE_API_URL` mà front-end vẫn URL cũ      | Dev server chưa đọc `.env` mới                             | Tắt `npm run dev` rồi chạy lại                                |
| `SECRET_KEY` trên GitHub                        | Commit `.env`                                              | `git rm --cached .env`                                        |

