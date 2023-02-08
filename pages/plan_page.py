from pages.locators import plan_page_loc as loc
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class PlanPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.plan_page_url = 'https://www.mynetdiary.com/plan.do'

    def open_plan_tab(self):
        self.click(loc.plan_tab)
        assert self.find(loc.weight_n_calories_tab).text == "Weight & Calories"
        return self.driver.current_url == self.plan_page_url

    def enter_current_weight_kg(self, current_weight):
        self.find(loc.current_weight).click()
        if self.find(loc.switcher).text == 'lb':
            self.click(loc.switcher)
            self.find(loc.check_box_kg_lb).click()
            self.click(loc.save_button)
        else:
            self.find(loc.switcher).is_displayed()
        self.find(loc.weight).send_keys(Keys.CONTROL + "a")
        self.find(loc.weight).send_keys(Keys.DELETE)
        self.send_keys(loc.weight, current_weight)
        self.click(loc.save_button)

    def verify_entered_weight(self, current_weight):
        return self.find_new_value(loc.current_weight, current_weight).get_attribute("value")

    def enter_empty_current_weight_kg(self):
        self.find(loc.current_weight).click()
        if self.find(loc.switcher).text == 'lb':
            self.click(loc.switcher)
            self.find(loc.check_box_kg_lb).click()
            self.click(loc.save_button)
        else:
            self.find(loc.switcher).is_displayed()
        self.find(loc.weight).send_keys(Keys.CONTROL + "a")
        self.find(loc.weight).send_keys(Keys.DELETE)
        self.click(loc.save_button)
        validation_error = self.find(loc.weight_validation_error).text
        return validation_error

    def validation_error_current_weight(self):
        validation_error = self.find(loc.weight_validation_error).text
        return validation_error

    def enter_current_weight_lb(self, current_weight):
        self.find(loc.current_weight).click()
        if self.find(loc.switcher).text == 'kg':
            self.click(loc.switcher)
            self.find(loc.check_box_kg_lb).click()
            self.click(loc.save_button)
        else:
            self.find(loc.switcher).is_displayed()
        self.find(loc.weight).send_keys(Keys.CONTROL + "a")
        self.find(loc.weight).send_keys(Keys.DELETE)
        self.send_keys(loc.weight, current_weight)
        self.click(loc.save_button)

    def enter_target_weight(self, target_weight):
        self.find(loc.target_weight).click()
        self.find(loc.target_weight_field).send_keys(Keys.CONTROL + "a")
        self.find(loc.target_weight_field).send_keys(Keys.DELETE)
        self.send_keys(loc.target_weight_field, target_weight)
        self.click(loc.save_button)

    def verify_entered_target_weight(self, target_weight):
        return self.find_new_value(loc.target_weight, target_weight).get_attribute("value")

    def validation_error_target_weight(self):
        validation_error = self.find(loc.target_weight_validation_error).text
        return validation_error

    def enter_next_year_target_date(self, year):
        self.click(loc.target_date)
        self.click(loc.year_button)
        self.click(loc.next_year)
        self.click(loc.ok_button)
        return self.find_new_value(loc.target_date, year).get_attribute("value")

    def enter_next_3_month_target_date(self, value):
        self.click(loc.target_date)
        self.click(loc.year_button)
        self.click(loc.current_year)
        self.click(loc.next_month)
        self.click(loc.next_month)
        self.click(loc.next_month)
        self.click(loc.ok_button)
        return self.find_new_value(loc.target_date, value).get_attribute("value")

    def change_1_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_1_radio_button).click()

    def change_2_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_2_radio_button).click()

    def change_3_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_3_radio_button).click()

    def change_4_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_4_radio_button).click()

    def change_5_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_5_radio_button).click()

    def change_6_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_6_radio_button).click()

    def change_7_weekly_rate(self):
        self.click(loc.weekly_rate)
        self.find(loc.change_weekly_rate_7_radio_button).click()

    def weekly_rate_value(self, value):
        return self.find_new_value(loc.weekly_rate, value).get_attribute("value")

    def enter_min_calorie_budget(self, value):
        self.click(loc.min_calorie_budget)
        self.find(loc.min_calorie_budget_input).send_keys(Keys.CONTROL + "a")
        self.find(loc.min_calorie_budget_input).send_keys(Keys.DELETE)
        self.send_keys(loc.min_calorie_budget_input, value)
        self.click(loc.save_button)

    def empty_min_calorie_budget(self):
        self.click(loc.min_calorie_budget)
        self.find(loc.min_calorie_budget_input).send_keys(Keys.CONTROL + "a")
        self.find(loc.min_calorie_budget_input).send_keys(Keys.DELETE)
        self.click(loc.save_button)

    def verify_min_calorie_budget(self, value):
        return self.find_new_value(loc.min_calorie_budget, value).get_attribute('value')

    def verify_empty_min_calorie_budget(self, value):
        self.no_value_in_locator(loc.min_calorie_budget, value)
        return True

    def enter_daily_food_calorie_budget(self, value):
        self.click(loc.daily_food_calorie_budget)
        self.find(loc.daily_food_calorie_budget_input).send_keys(Keys.CONTROL + "a")
        self.find(loc.daily_food_calorie_budget_input).send_keys(Keys.DELETE)
        self.send_keys(loc.min_calorie_budget_input, value)
        self.click(loc.save_button)

    def verify_daily_food_calorie_budget(self, value):
        return self.find_new_value(loc.daily_food_calorie_budget, value).get_attribute('value')

    def verify_empty_daily_food_calorie_budget_error(self):
        return self.find(loc.empty_daily_food_calorie_budget_error).text

    def click_send_feedback_button(self):
        self.scroll_to_bottom()
        return self.click(loc.send_feedback_button)

    def is_displayed_feedback_form(self):
        return self.find(loc.feedback_form).text

    def click_recommend_button(self):
        self.scroll_to_bottom()
        return self.click(loc.recommend_button)

    def verify_lose_weight_safely_page_opened(self):
        return self.find(loc.lose_weight_safely).text
