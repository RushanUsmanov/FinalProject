from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):
    def click_basket_button(self):
        basket = self.browser.find_element(*Basket.BASKET)
        basket.click()

    def should_be_product_page(self):
        self.should_be_name_of_item()
        self.should_be_price_of_item()

    def should_be_name_of_item(self):
        assert self.is_element_present(*NameProduct.ITEM), "name of item missing"
        assert self.is_element_present(
            *NameProductAfterAddInBasket.ITEM_AFTER), "name item after add in basket missing"
        product_name = self.browser.find_element(*NameProduct.ITEM).text
        message_after_add = self.browser.find_element(*NameProductAfterAddInBasket.ITEM_AFTER).text
        assert product_name in message_after_add, "product name missing in message after add"

    def should_be_price_of_item(self):
        assert self.is_element_present(*PriceProduct.PRICE), "price of item missing"
        assert self.is_element_present(
            *PriceProductAfterAddInBasket.PRICE_AFTER), "price item after add in basket missing"
        product_price = self.browser.find_element(*PriceProduct.PRICE).text
        message_after_add = self.browser.find_element(*PriceProductAfterAddInBasket.PRICE_AFTER).text
        assert product_price in message_after_add, "price item missing in message after add"
