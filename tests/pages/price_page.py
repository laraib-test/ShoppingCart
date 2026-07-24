from pages.base_page import BasePage

class PricePage(BasePage):

    def select_category(self, value):
        self.page.locator("#id_category").select_option(value)

    def set_price(self, price):
        self.page.get_by_placeholder(
            "$ Enter price"
        ).fill(price)

    def save(self):
        self.page.get_by_role(
            "button",
            name="💾 Save Price"
        ).click()