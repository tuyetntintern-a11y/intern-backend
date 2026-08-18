from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.models import Category, Book
from app.schemas.category import CategoryCreate, CategoryUpdate


def list_categories(db: Session) -> list[Category]:
    statement = select(Category).order_by(Category.id)

    return db.scalars(statement).all()


def get_category(
    db: Session,
    category_id: int,
) -> Category:
    category = db.get(Category, category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return category


def create_category(
    db: Session,
    payload: CategoryCreate,
) -> Category:
    category = Category(name=payload.name)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def update_category(
    db: Session,
    category_id: int,
    payload: CategoryUpdate,
) -> Category:
    category = get_category(db, category_id)

    category.name = payload.name

    db.commit()
    db.refresh(category)

    return category


def delete_category(
    db: Session,
    category_id: int,
) -> None:
    category = get_category(db, category_id)

    category_count = db.scalar(select(func.count()).select_from(Book).
                               where(Book.category_id == category_id))
    
    if category_count > 0:
        raise HTTPException(
               status_code=409,
               detail="Cannot delete category while books exist",
           )

    db.delete(category)
    db.commit()