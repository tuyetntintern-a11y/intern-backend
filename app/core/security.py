import bcrypt

from datetime import datetime, timedelta, timezone

import jwt

from app.core.config import get_settings




def hash_password(plain: str) -> str:
    # hash_password  = tạo hash để lưu vào database.encode("utf-8") ma hoa thanh dang bytes
    return bcrypt.hashpw(
        plain.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    # verify_password = kiểm tra mật khẩu đăng nhập với hash đã lưu
    return bcrypt.checkpw(
        plain.encode("utf-8"),
        hashed.encode("utf-8"),
    )


def create_access_token(subject: str) -> str:
    settings = get_settings()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload = {"sub": subject, "exp": expire}

    return jwt.encode(payload, 
                      settings.secret_key, 
                      algorithm=settings.jwt_algorithm
                      )