from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, link)
    login.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_button_basket()
    page.should_be_empty_basket()
    page.should_not_disappear()
