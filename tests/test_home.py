from pages.home_page import HomePage

def test_homepage(page):

    home = HomePage(page)

    home.open()

    assert home.get_title() != ""