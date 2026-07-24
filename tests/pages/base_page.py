class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png")