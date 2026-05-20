import pytest
from pages.books_page import BooksPage

@pytest.fixture
def books(page):
    p=BooksPage(page)
    p.navigate()
    return p
def test_homepage_title(books):
    title=books.get_page_title()
    assert "Books to Scrape" in title
def test_book_title(books):
    titles=books.get_book_titles()
    assert len(titles)==20
def test_prices_have_currency_symbol(books):
    prices=books.get_book_prices()
    for price in prices:
        assert "£" in price, f"Prices without £ symbol:{price}"
def test_star_rating_exist(books):
    ratings=books.get_star_ratings()
    assert len(ratings)==20
def test_category_navigation(books,page):
    books.search_category("mystery")
    assert "mystery" in page.url.lower()
def test_prices_are_positive(books):
    pea=books.get_book_prices()
    for price in pea:
        price_value=float(price.replace("£",""))
        assert price_value>0, f"Price should be positive:{price}"
