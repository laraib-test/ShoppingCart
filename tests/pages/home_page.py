class HomePage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("http://127.0.0.1:8009/")

    def get_title(self):
        return self.page.title()