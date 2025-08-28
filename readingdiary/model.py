from datetime import datetime

class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:

