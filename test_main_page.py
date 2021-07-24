from .pages.main_page import MainPage
from .pages.login_page import *


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    login = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
<<<<<<< HEAD
    page.should_be_login_link()
    login.should_be_login_page()
=======
    page.should_be_login_link()
>>>>>>> parent of e445786 (Add files from lesson 4.2 step 6)
