from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    basket = ProductPage(browser, link)
    basket.open()
    basket.click_basket_button()
    basket.solve_quiz_and_get_code()
    basket.should_be_product_page()
