from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_basket_button(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def should_be_product_page(self):
        self.should_be_name_of_item()
        self.should_be_price_of_item()

    def should_be_name_of_item(self):
        assert self.is_element_present(*ProductPageLocators.NAME_ITEM), "name of item missing"
        assert self.is_element_present(
            *ProductPageLocators.NAME_ITEM_AFTER_ADD), "name item after add in basket missing"
        product_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM).text
        message_after_add = self.browser.find_element(*ProductPageLocators.NAME_ITEM_AFTER_ADD).text
        assert product_name == message_after_add, "product name missing in message after add"

    def should_be_price_of_item(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "price of item missing"
        assert self.is_element_present(
            *ProductPageLocators.PRICE_AFTER_ADD), "price item after add in basket missing"
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        message_after_add = self.browser.find_element(*ProductPageLocators.PRICE_AFTER_ADD).text
        assert product_price == message_after_add, "price item missing in message after add"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, " \
                                                                                   "but should not be "

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, " \
                                                                                   "but should be disappear"
