import bcrypt


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