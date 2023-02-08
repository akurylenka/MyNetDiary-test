from pages.locators import food_page_loc as loc
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class FoodPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.food_page_url = 'https://www.mynetdiary.com/meals.do'

    def open_food_tab(self):
        self.click(loc.food_tab)
        assert self.driver.current_url == self.food_page_url

    def add_food(self, option_id, food):
        self.find_all(loc.add_button)[option_id].click()
        self.click(loc.search_button)
        self.send_keys(loc.enter_breakfast_food, food)
        self.click(loc.click_on_food_from_search)
        self.find(loc.log_food_to).send_keys(Keys.ENTER)

    def click_on_add_breakfast_button(self):
        self.find_all(loc.add_button)[0].click()

    def click_on_search_button(self):
        self.click(loc.search_button)

    def click_on_settings_button(self):
        self.click(loc.settings_button)

    def click_on_back_to_meals_button(self):
        self.click(loc.back_to_meals_button)

    def add_egg_to_breakfast(self):
        self.send_keys(loc.enter_breakfast_food, "Boiled egg")
        self.click(loc.click_on_food_from_search)
        self.find(loc.log_food_to).send_keys("1")
        self.find(loc.log_food_to).send_keys(Keys.ENTER)

    def check_egg_added_to_food(self):
        return self.text_is_present(loc.product_egg, "Boiled egg").text

    def add_green_apple_to_breakfast(self):
        self.send_keys(loc.enter_breakfast_food, "Green apple")
        self.click(loc.click_on_food_from_search)
        self.find(loc.log_food_to).send_keys("1")
        self.find(loc.log_food_to).send_keys(Keys.ENTER)

    def delete_apple_breakfast(self):
        ActionChains(self.driver).move_to_element(self.find(loc.product_green_apple)).perform()
        self.find(loc.product_green_apple).click()
        self.click(loc.delete_button)

    def check_deleted_food(self):
        self.no_locator(loc.product_green_apple)
        return True

    def is_displayed_plus_icon(self):
        return self.is_displayed(loc.plus_button)

    def is_displayed_food_entry_settings(self):
        return self.is_displayed(loc.food_entry_settings)

    def log_calories_quickly(self, calories_number):
        self.click(loc.quick_button)
        self.send_keys(loc.calories_input, calories_number)
        self.click(loc.save_button)

    def is_displayed_generic_food_calories(self):
        self.text_to_be_present(loc.calories, "21 calorie")
        generic_food_calories = self.find(loc.calories).text
        return generic_food_calories

    def add_coffee_to_food(self, option_id, food):
        self.find_all(loc.add_button)[option_id].click()
        self.click(loc.search_button)
        self.send_keys(loc.enter_breakfast_food, food)
        self.click(loc.click_on_food_from_search)
        self.find(loc.log_food_to).send_keys(Keys.ENTER)
        self.visibility_of_all_elements(loc.added_coffee)

    def is_displayed_added_coffee(self):
        return self.is_displayed(loc.added_coffee)

    def delete_quick_calories(self):
        ActionChains(self.driver).move_to_element(self.find(loc.added_100_calories)).perform()
        self.find(loc.added_100_calories).click()
        self.click(loc.delete_button)

    def check_deleted_calories(self):
        self.no_locator(loc.added_100_calories)
        return True
