from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Функция для перехода по кнопке корзины в шапке сайта
    def go_to_button_basket(self):
        button = self.browser.find_element(*BasePageLocators.BUTTON_BASKET)
        button.click()

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY)

    def should_not_disappear(self):
        assert self.is_disappeared(*BasketPageLocators.MESSAGE_EMPTY) == False, "item is missing"
