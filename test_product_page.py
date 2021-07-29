import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    basket = ProductPage(browser, link)
    basket.open()
    basket.click_basket_button()
    basket.solve_quiz_and_get_code()
    basket.should_be_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
    basket = ProductPage(browser, link)
    basket.open()
    basket.click_basket_button()
    basket.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
    basket = ProductPage(browser, link)
    basket.open()
    basket.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
    basket = ProductPage(browser, link)
    basket.open()
    basket.click_basket_button()
    basket.should_disappear_success_message()
