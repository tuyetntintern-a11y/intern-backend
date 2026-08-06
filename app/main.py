# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel


# app = FastAPI(title="Books API")

# @app.get("/")
# def hello_world():
#     return {"message": "Hello World"}
# class Book(BaseModel):
#     title: str
#     author: str
#     year: int

# # luu tam trong RAM
# books: dict[int, Book] = {}


# @app.get("/books")
# def list_books():
#     result = []
#     for book_id, book in books.items():
#         result.append({
#             "id": book_id,
#             "title": book.title,
#             "author": book.author,
#             "year": book.year
#         })
#     return result


# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     book = books.get(book_id)
#     if book is None:
#         raise HTTPException(status_code=404, detail="Book not found")
#     else:
#         return{
#             "id": book_id,
#                     "title": book.title,
#                     "author": book.author,
#                     "year": book.year}



# @app.post("/books", status_code=201)
# def create_book(book: Book):
#     book_id = max(books.keys(), default= 0) + 1
#     books[book_id] = book
#     return{
#         "id": book_id,
#                         "title": book.title,
#                         "author": book.author,
#                         "year": book.year
#                         }

# @app.put("/books/{book_id}")
# def update_book(book_id: int, book: Book):
#     if book_id not in books:
#         raise HTTPException(
#             status_code=404, 
#             detail="Book not found")

#     books[book_id] = book
#     return{
#             "id": book_id,
#             "title": book.title,
#             "author": book.author,
#             "year": book.year
#         }


# @app.delete("/books/{book_id}", status_code=204)
# def delete_book(book_id: int):
#     if book_id not in books:
#         raise HTTPException(
#             status_code=404, 
#             detail="Book not found")
#     else:
#         del books[book_id]
#     return None

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Book
from app.admin import setup_admin

app = FastAPI(title="Books API")
Base.metadata.create_all(bind=engine)
setup_admin(app, engine)


class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    summary: str

@app.get("/")
def root():
    return {"message": "HELLO WORLD"}

@app.get("/books")
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()



@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if book is None:
            raise(HTTPException(status_code=404,
                                 detail="Book not found"))
    return book


@app.post("/books", status_code=201)
def create_book(payload: BookCreate, db:Session = Depends(get_db)):
    
    book = Book(title=payload.title,
                author=payload.author,
                year=payload.year,
                summary=payload.summary
                )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookCreate, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if book is None:
          raise HTTPException(status_code=404, detail="Book not foynd")

    book.title = payload.title
    book.author = payload.author
    book.year = payload.year
    book.summary = payload.summary
    
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return None    