from pages.base_page import BasePage

class ProductPage(BasePage):

    def open_milk(self):
        self.page.get_by_role(
            "img",
            name="Milk"
        ).click()

    def add_to_cart(self):
        self.page.get_by_role(
            "button",
            name="🛒 Add to Cart"
        ).click()

    def click_edit_price(self):
        self.page.get_by_role(
            "link",
            name="✏"
        ).first.click()