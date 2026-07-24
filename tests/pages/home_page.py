from pages.base_page import BasePage

class HomePage(BasePage):

    URL = "http://127.0.0.1:8009/"

    def open(self):
        self.page.goto(self.URL)

    def click_browse_products(self):
        self.page.get_by_role(
            "link",
            name="🛍 Browse Products"
        ).click()

    def title(self):
        return self.page.title()