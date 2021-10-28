import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

PAGES_DIR = "pages"
BOOKS_ON_PAGE = 10


def render():
    os.makedirs(PAGES_DIR, exist_ok=True)

    with open("books.json") as index:
        catalog = json.load(index)

    template = env.get_template("template.html")
    books_on_page = list(chunked(catalog, BOOKS_ON_PAGE))
    for num, page in enumerate(books_on_page, start=1):
        books = list(chunked(page, BOOKS_ON_PAGE // 2))
        rendered_page = template.render(
            books=books, num_pages=len(books_on_page), current=num
        )
        with open(
            os.path.join(PAGES_DIR, f"index{num}.html"), "w", encoding="utf8"
        ) as file:
            file.write(rendered_page)


if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader("."), autoescape=select_autoescape(["html"])
    )
    render()
