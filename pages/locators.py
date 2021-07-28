from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[id='login_form']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[id='register_form']")


class Basket():
    BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")


class NameProduct():
    ITEM = (By.CSS_SELECTOR, ".product_main h1")


class NameProductAfterAddInBasket():
    ITEM_AFTER = (By.CSS_SELECTOR, ".alertinner strong")


class PriceProduct():
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class PriceProductAfterAddInBasket():
    PRICE_AFTER = (By.CSS_SELECTOR, ".alertinner p strong")
