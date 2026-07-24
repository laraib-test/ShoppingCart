from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.price_page import PricePage

def test_update_price(page):

    home = HomePage(page)
    product = ProductPage(page)
    price = PricePage(page)

    home.open()

    home.click_browse_products()

    product.open_milk()

    product.click_edit_price()

    price.select_category("4")

    price.set_price("5.09")

    price.save()