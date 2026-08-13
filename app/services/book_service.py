from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import Author, Book
from app.schemas.book import BookCreate, BookRead, BookUpdate


def to_book_read(book: Book) -> BookRead:
    return BookRead(
        id=book.id,
        title=book.title,
        year=book.year,
        summary=book.summary,
        author_id=book.author_id,
        author_name=book.author.name if book.author else None,
    )


def _ensure_author_exists(
    db: Session,
    author_id: int | None,
) -> None:
    if author_id is None:
        return

    author = db.get(Author, author_id)

    if author is None:
        raise HTTPException(
            status_code=404,
            detail="Author not found",
        )


def _get_book_model(
    db: Session,
    book_id: int,
) -> Book:
    statement = (
        select(Book)
        .options(joinedload(Book.author))
        .where(Book.id == book_id)
    )

    book = db.scalar(statement)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return book


def list_books(db: Session) -> list[BookRead]:
    statement = (
        select(Book)
        .options(joinedload(Book.author))
        .order_by(Book.id)
    )

    books = db.scalars(statement).all()

    return [to_book_read(book) for book in books]


def get_book(
    db: Session,
    book_id: int,
) -> BookRead:
    book = _get_book_model(db, book_id)

    return to_book_read(book)


def create_book(
    db: Session,
    payload: BookCreate,
) -> BookRead:
    _ensure_author_exists(db, payload.author_id)

    book = Book(
        title=payload.title,
        year=payload.year,
        summary=payload.summary,
        author_id=payload.author_id,
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    created_book = _get_book_model(db, book.id)

    return to_book_read(created_book)


def update_book(
    db: Session,
    book_id: int,
    payload: BookUpdate,
) -> BookRead:
    book = _get_book_model(db, book_id)

    _ensure_author_exists(db, payload.author_id)

    book.title = payload.title
    book.year = payload.year
    book.summary = payload.summary
    book.author_id = payload.author_id

    db.commit()
    db.refresh(book)

    updated_book = _get_book_model(db, book.id)

    return to_book_read(updated_book)


def delete_book(
    db: Session,
    book_id: int,
) -> None:
    book = _get_book_model(db, book_id)

    db.delete(book)
    db.commit()


def list_books_by_author(
    db: Session,
    author_id: int,
) -> list[BookRead]:
    _ensure_author_exists(db, author_id)

    statement = (
        select(Book)
        .options(joinedload(Book.author))
        .where(Book.author_id == author_id)
        .order_by(Book.id)
    )

    books = db.scalars(statement).all()

    return [to_book_read(book) for book in books]