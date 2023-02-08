from pages.food_page import FoodPage
import allure
import pytest


@allure.feature('Food page')
@allure.story('Plus icon')
def test_plus_icon_is_displayed(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Verify food page opened with plus icon'):
        assert food_page.is_displayed_plus_icon()


@allure.feature('Food page')
@allure.story('Check Back to meals button clickable')
def test_back_to_meals_button(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Click Add button'):
        food_page.click_on_add_breakfast_button()
    with allure.step('Click Search button'):
        food_page.click_on_search_button()
    with allure.step('Click Back to meals button'):
        food_page.click_on_back_to_meals_button()
    with allure.step('Verify food page opened with plus icon'):
        assert food_page.is_displayed_plus_icon()


@allure.feature('Food page')
@allure.story('Add quick calories')
def test_add_quick_calories(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Click Add button'):
        food_page.click_on_add_breakfast_button()
    with allure.step('Log Quick calories'):
        food_page.log_calories_quickly("21")
    with allure.step('Verify Generic food calories were added'):
        assert food_page.is_displayed_generic_food_calories() == "21 calorie"


@allure.feature('Food page')
@allure.story('Delete quick calories')
def test_delete_quick_calories(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Click Add button'):
        food_page.click_on_add_breakfast_button()
    with allure.step('Log Quick calories'):
        food_page.log_calories_quickly("100")
    with allure.step('Delete quick calories'):
        food_page.delete_quick_calories()
    with allure.step('Verify quick calories were deleted'):
        assert food_page.check_deleted_food()


@allure.feature('Food page')
@allure.story('Add breakfast')
def test_add_breakfast(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Click Add button'):
        food_page.click_on_add_breakfast_button()
    with allure.step('Click Search button'):
        food_page.click_on_search_button()
    with allure.step('Add breakfast'):
        food_page.add_egg_to_breakfast()
    with allure.step('Verify breakfast was added'):
        assert food_page.check_egg_added_to_food()


@allure.feature('Food page')
@allure.story('Delete breakfast')
def test_delete_breakfast(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Click Add button'):
        food_page.click_on_add_breakfast_button()
    with allure.step('Click Search button'):
        food_page.click_on_search_button()
    with allure.step('Add breakfast'):
        food_page.add_green_apple_to_breakfast()
    with allure.step('Delete breakfast'):
        food_page.delete_apple_breakfast()
    with allure.step('Verify breakfast was deleted'):
        assert food_page.check_deleted_food()


@allure.feature('Food page')
@allure.story('Check Settings button clickable')
def test_click_settings_button(driver, auth):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Click Add button'):
        food_page.click_on_add_breakfast_button()
    with allure.step('Click Search button'):
        food_page.click_on_search_button()
    with allure.step('Click Settings button'):
        food_page.click_on_settings_button()
    with allure.step('Verify food entry settings page is displayed'):
        assert food_page.is_displayed_food_entry_settings()


@allure.feature('Food page')
@allure.story('Add breakfast, lunch, dinner, snacks')
@pytest.mark.parametrize('option_id', list(range(0, 4)))
def test_add_food(driver, auth, option_id):
    with allure.step('Open food page'):
        food_page = FoodPage(driver)
        food_page.open_food_tab()
    with allure.step('Add food'):
        food_page.add_coffee_to_food(option_id, "coffee")
    with allure.step('Verify added food'):
        assert food_page.is_displayed_added_coffee()
