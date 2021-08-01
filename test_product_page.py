import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = email
        link_login = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link_login)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
        page = ProductPage(browser, link_promo)
        page.open()
        page.click_basket_button()
        page.solve_quiz_and_get_code()
        page.should_be_product_page()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# Оставил параметризацию, считаю это важным кейсом и не хочу потерять его, на оценку ревью влиять не должно
@pytest.mark.parametrize('link_iterate', [0, 1, 2, 3, 4, 5, 6,
                                          pytest.param(7, marks=pytest.mark.xfail),
                                          8, 9])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link_iterate):
    link_iterate = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_iterate}"
    page = ProductPage(browser, link_iterate)
    page.open()
    page.click_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_button_basket()
    page.should_be_empty_basket()
    page.should_not_disappear()
