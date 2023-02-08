from selenium.webdriver.common.by import By

food_tab = (By.XPATH, '//span[text()="Food"]')

plus_button = (By.XPATH, '//button[@title="Click here to start logging"]')
add_button = (By.XPATH, '//span[text()="Add"]')
quick_button = (By.XPATH, '//span[text()="Quick"]')
search_button = (By.XPATH, '(//span[text()="Search"])')
back_to_meals_button = (By.XPATH, '(//span[text()="Back to Meals"])')
delete_button = (By.XPATH, '//span[text()="Delete Entry"]')
settings_button = (By.XPATH, '(//span[text()="Settings"])[2]')
save_button = (By.XPATH, '//span[text()="Save"]')
log_food_to = (By.XPATH, '//label[text()="Amount eaten"]/../div/input')

enter_breakfast_food = (By.XPATH, '//label[text()="Please enter food name, brand or restaurant name"]/../div/input')
click_on_food_from_search = (By.XPATH, '//div[@role="button"]/div[2]/span/div/div[1]')
calories_input = (By.NAME, "quickCalories")
food_entry_settings = (By.XPATH, '//span[text()="Food Entry Settings"]')

coffee = (By.CLASS_NAME, 'MuiListItemIcon-root-3899')
product_egg = (By.XPATH, '//div[text()="Boiled egg"]')
product_green_apple = (By.XPATH, '//div[text()="Green apple"]')
added_coffee = (By.XPATH, '//div[text()="Coffee"]')
calories = (By.XPATH, '//span[text()="21 calorie"]')
added_100_calories = (By.XPATH, '(//span[text()="100 calorie"])[1]')
