from selenium.webdriver.common.by import By

plan_tab = (By.XPATH, '//span[text()="Plan"]')
weight_n_calories_tab = (By.XPATH, '//span[text()="Weight & Calories"]')

current_weight = (By.XPATH, '(//input[@class="MuiInputBase-input-253 MuiInput-input-239"])[1]')
target_weight = (By.XPATH, '(//input[@class="MuiInputBase-input-253 MuiInput-input-239"])[2]')
target_date = (By.XPATH, '(//input[@class="MuiInputBase-input-253 MuiInput-input-239"])[3]')
weekly_rate = (By.XPATH, '(//input[@class="MuiInputBase-input-253 MuiInput-input-239"])[4]')
daily_food_calorie_budget = (By.XPATH, '(//input[@class="MuiInputBase-input-253 MuiInput-input-239"])[5]')
min_calorie_budget = (By.XPATH, '(//input[@class="MuiInputBase-input-253 MuiInput-input-239"])[6]')

switcher = (By.XPATH, '//p/div[1]/span')
check_box_kg_lb = (By.XPATH, '//input[@type="checkbox"]')
weight = (By.NAME, 'weightField')
weight_validation_error = (By.XPATH, '//input[@name="weightField"]/../../p')
target_weight_kg = (By.CLASS_NAME, 'MuiTypography-h6-2943')
target_weight_field = (By.NAME, 'planField')
target_weight_validation_error = (By.XPATH, '//input[@name="planField"]/../../p')
save_button = (By.XPATH, '//span[text()="Save"]')

year_button = (By.TAG_NAME, 'h6')
current_year = (By.XPATH, '//div[text()="2023"]')
next_year = (By.XPATH, '//div[text()="2024"]')
next_month = (
    By.XPATH,
    '//p[@class="MuiTypography-root-139 MuiTypography-body1-141 MuiTypography-alignCenter-155"]/../../button[2]'
)
ok_button = (By.XPATH, '//span[text()="OK"]')

change_weekly_rate_1_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[1]')
change_weekly_rate_2_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[2]')
change_weekly_rate_3_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[3]')
change_weekly_rate_4_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[4]')
change_weekly_rate_5_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[5]')
change_weekly_rate_6_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[6]')
change_weekly_rate_7_radio_button = (By.XPATH, '(//input[@name="radioDiallog"])[7]')

min_calorie_budget_input = (By.NAME, 'planField')
daily_food_calorie_budget_input = (By.NAME, 'planField')
send_feedback_button = (By.XPATH, '//span[text()="Send Feedback"]')
feedback_form = (By.XPATH, '//h2')
empty_daily_food_calorie_budget_error = (By.XPATH, '//p[text()="Please enter your Daily Food Calorie Budget"]')
recommend_button = (By.XPATH, '//span[text()="Recommend"]')
lose_weight_safely = (By.XPATH, '//h2[@class="MuiTypography-root-139 MuiTypography-h6-149"]')
