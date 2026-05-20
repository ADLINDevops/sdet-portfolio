class BooksPage:
    URL = "https://books.toscrape.com"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)

    def get_book_titles(self):
        return self.page.locator("h3 a").all_text_contents()

    def get_book_prices(self):
        return self.page.locator(".price_color").all_text_contents()

    def get_star_ratings(self):
        return self.page.locator(".star-rating").all()

    def search_category(self, category_name):
        self.page.locator(f"a:text('{category_name}')").click()

    def get_page_title(self):
        return self.page.title()