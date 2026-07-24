from pages.base_page import BasePage

class CartPage(BasePage):

    def cart_count(self):
        return self.page.locator(".badge").inner_text()

    def checkout(self):
        self.page.get_by_role(
            "button",
            name="Checkout"
        ).click()