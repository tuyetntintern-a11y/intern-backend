from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import Author, Book, Category
from app.schemas.book import BookCreate, BookRead, BookUpdate


def to_book_read(book: Book) -> BookRead:
    return BookRead(
        id=book.id,
        title=book.title,
        year=book.year,
        summary=book.summary,
        author_id=book.author_id,
        author_name=book.author.name if book.author else None,
        category_id=book.category_id,
        category_name=book.category.name if book.category else None,
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


def _ensure_category_exists(
    db: Session,
    category_id: int | None,
) -> None:
    if category_id is None:
        return

    category = db.get(Category, category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )


def _get_book_model(
    db: Session,
    book_id: int,
) -> Book:
    statement = (
        select(Book)
        .options(
            joinedload(Book.author),
            joinedload(Book.category),
        )
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
        .options(
            joinedload(Book.author),
            joinedload(Book.category),
        )
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
    _ensure_category_exists(db, payload.category_id)

    book = Book(
        title=payload.title,
        year=payload.year,
        summary=payload.summary,
        author_id=payload.author_id,
        category_id=payload.category_id,
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
    _ensure_category_exists(db, payload.category_id)

    book.title = payload.title
    book.year = payload.year
    book.summary = payload.summary
    book.author_id = payload.author_id
    book.category_id = payload.category_id

    db.commit()

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
        .options(
            joinedload(Book.author),
            joinedload(Book.category),
        )
        .where(Book.author_id == author_id)
        .order_by(Book.id)
    )

    books = db.scalars(statement).all()

    return [to_book_read(book) for book in books]

def search_books(
    db: Session,
    *,
    author_id: int | None = None,
    category_id: int | None = None,
    year_from: int | None = None,
    year_to: int | None = None,
    q: str | None = None,
) -> list[BookRead]:
    statement = select(Book).options(
        joinedload(Book.author),
        joinedload(Book.category),
    )
    if author_id is not None:
        statement = statement.where(Book.author_id == author_id)
    if category_id is not None:
        statement=statement.where(Book.category_id == category_id)
    if year_from is not None:
        statement = statement.where(Book.year >= year_from)
    if year_to is not None:
        statement = statement.where(Book.year <= year_to)
    if q:
        statement = statement.where(Book.title.ilike(f"%{q}%"))

    statement = statement.order_by(Book.id)

    books = db.scalars(statement).all()

    return [to_book_read(book) for book in books]