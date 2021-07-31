from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[id='login_form']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[id='register_form']")


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    NAME_ITEM_AFTER_ADD = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_AFTER_ADD = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class BasketPageLocators():
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")