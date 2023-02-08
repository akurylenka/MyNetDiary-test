from pages.plan_page import PlanPage
import allure
import pytest

WEIGHT_KG = [
    ('55', '55 kg'),
    ('55.5', '55.5 kg'),
    ('55.88888', '55.9 kg'),
    ('55.22222', '55.2 kg')
]

WEIGHT_LB = [
    ('110', '110 lb'),
    ('110.5', '110.5 lb'),
    ('110.88888', '110.9 lb'),
    ('110.22222', '110.2 lb')
]


@allure.feature('Plan page')
@allure.story('Plan page link')
def test_is_plan_tab_opened(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Check that plan page is opened'):
        assert plan_page.plan_page_url == 'https://www.mynetdiary.com/plan.do'


@allure.feature('Plan page')
@allure.story('Valid current weight in kg')
@pytest.mark.parametrize('weight', WEIGHT_KG)
def test_enter_valid_weight_in_kg(driver, auth, weight):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Enter current weight in kg'):
        weight_value, weight_check = weight
        plan_page.enter_current_weight_kg(weight_value)
    with allure.step('Verify that weight is displayed'):
        assert plan_page.verify_entered_weight(weight_check) == weight_check


@allure.feature('Plan page')
@allure.story('Empty current weight error')
def test_empty_weight_in_kg_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter empty current weight and check error'):
        assert plan_page.enter_empty_current_weight_kg() == 'Please enter your weight in kg, e.g 70.5'


@allure.feature('Plan page')
@allure.story('Low value current weight in kg error')
def test_low_weight_in_kg_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter low current weight in kg'):
        plan_page.enter_current_weight_kg("24")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_current_weight() == "Please enter numeric weight greater than 25 kg."


@allure.feature('Plan page')
@allure.story('Big value current weight in kg error')
def test_big_weight_in_kg_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter big current weight in kg'):
        plan_page.enter_current_weight_kg("454")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_current_weight() == "Please enter a realistic smaller weight in kg."


@allure.feature('Plan page')
@allure.story('Valid current weight in lb')
@pytest.mark.parametrize('weight', WEIGHT_LB)
def test_enter_valid_weight_in_lb(driver, auth, weight):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Enter current weight in lb'):
        weight_value, weight_check = weight
        plan_page.enter_current_weight_lb(weight_value)
    with allure.step('Verify that weight is displayed'):
        assert plan_page.verify_entered_weight(weight_check) == weight_check


@allure.feature('Plan page')
@allure.story('Low value current weight in lb error')
def test_low_weight_in_lb_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter low current weight in lb'):
        plan_page.enter_current_weight_lb("45")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_current_weight() == "Please enter numeric weight greater than 50 lbs."


@allure.feature('Plan page')
@allure.story('Big value current weight in lb error')
def test_big_weight_in_lb_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter big current weight in lb'):
        plan_page.enter_current_weight_lb("1000")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_current_weight() == "Please enter a realistic smaller weight in pounds."


@allure.feature('Plan page')
@allure.story('Low value target weight in kg error')
def test_low_target_weight_in_kg_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kg'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter low target weight in kg'):
        plan_page.enter_target_weight("10")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_target_weight() == 'Please enter numeric weight greater than 25 kg.'


@allure.feature('Plan page')
@allure.story('Big value target weight in kg error')
def test_big_target_weight_in_kg_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kg'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("454")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_target_weight() == 'Please enter a realistic smaller weight in kg.'


@allure.feature('Plan page')
@allure.story('Valid target weight in kg')
def test_enter_valid_target_weight_in_kg(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter valid target weight in kb'):
        plan_page.enter_target_weight("50")
    with allure.step('Verify that weight is displayed'):
        assert plan_page.verify_entered_target_weight('50 kg') == '50 kg'


@allure.feature('Plan page')
@allure.story('Valid target weight in lb')
def test_enter_valid_target_weight_in_lb(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in lb'):
        plan_page.enter_current_weight_lb("121")
    with allure.step('Enter valid target weight in lb'):
        plan_page.enter_target_weight("110")
    with allure.step('Verify that weight is displayed'):
        assert plan_page.verify_entered_target_weight('110 lb') == '110 lb'


@allure.feature('Plan page')
@allure.story('Low value target weight in lb error')
def test_low_target_weight_in_lb_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in lb'):
        plan_page.enter_current_weight_lb("121")
    with allure.step('Enter low target weight in lb'):
        plan_page.enter_target_weight("49")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_target_weight() == 'Please enter numeric weight greater than 50 lbs.'


@allure.feature('Plan page')
@allure.story('Big value target weight in lb error')
def test_big_target_weight_in_lb_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in lb'):
        plan_page.enter_current_weight_lb("121")
    with allure.step('Enter big target weight in lb'):
        plan_page.enter_target_weight("1000")
    with allure.step('Verify validation error is displayed'):
        assert plan_page.validation_error_target_weight() == 'Please enter a realistic smaller weight in pounds.'


@allure.feature('Plan page')
@allure.story('Next year target date')
def test_enter_valid_target_date(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter next year target date'):
        assert '2024' in plan_page.enter_next_year_target_date('2024')


@allure.feature('Plan page')
@allure.story('Change target date')
def test_change_target_date(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter next 3 month target date'):
        target_date_value = plan_page.enter_next_3_month_target_date('2023')
    with allure.step('Enter next year target date'):
        assert plan_page.enter_next_year_target_date('2024') != target_date_value


@allure.feature('Plan page')
@allure.story('Enter min calorie budget')
def test_enter_min_calorie_budget(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter min calorie budget'):
        plan_page.enter_min_calorie_budget("700")
    with allure.step('Verify min calorie budget was added'):
        assert plan_page.verify_min_calorie_budget("700") == "700"


@allure.feature('Plan page')
@allure.story('Empty min calorie budget')
def test_enter_empty_min_calorie_budget(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter min calorie budget'):
        plan_page.enter_min_calorie_budget("800")
    with allure.step('Enter min calorie budget'):
        plan_page.empty_min_calorie_budget()
    with allure.step('Verify empty min calorie budget was added'):
        assert plan_page.verify_empty_min_calorie_budget("800")


@allure.feature('Plan page')
@allure.story('Enter Daily food calorie budget')
def test_enter_daily_food_calorie_budget(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter Daily food calorie budget'):
        plan_page.enter_daily_food_calorie_budget("1600")
    with allure.step('Verify Daily food calorie budget is displayed'):
        assert plan_page.verify_daily_food_calorie_budget("1,600") == "1,600"


@allure.feature('Plan page')
@allure.story('Empty Daily food calorie budget error')
def test_empty_daily_food_calorie_budget_error(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter Daily food calorie budget'):
        plan_page.enter_daily_food_calorie_budget("")
    with allure.step('Verify Daily food calorie budget error is displayed'):
        assert plan_page.verify_empty_daily_food_calorie_budget_error() == "Please enter your Daily Food Calorie Budget"


@allure.feature('Plan page')
@allure.story('Change weekly rate to losing 1 kg per week')
def test_change_weekly_rate_losing_1_kg(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_1_weekly_rate()
    with allure.step('Verify losing 1 kg per week was set'):
        assert plan_page.weekly_rate_value("losing 1 kg per week") == "losing 1 kg per week"


@allure.feature('Plan page')
@allure.story('Change weekly rate to losing 0.75 kg per week')
def test_change_weekly_rate_losing_750_g(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_2_weekly_rate()
    with allure.step('Verify losing 0.75 kg per week was set'):
        assert plan_page.weekly_rate_value("losing 0.75 kg per week") == "losing 0.75 kg per week"


@allure.feature('Plan page')
@allure.story('Change weekly rate to losing 0.5 kg per week')
def test_change_weekly_rate_losing_500_g(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_3_weekly_rate()
    with allure.step('Verify losing 0.5 kg per week was set'):
        assert plan_page.weekly_rate_value("losing 0.5 kg per week") == "losing 0.5 kg per week"


@allure.feature('Plan page')
@allure.story('Change weekly rate to losing 0.33 kg per week')
def test_change_weekly_rate_losing_330_g(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_4_weekly_rate()
    with allure.step('Verify losing 0.33 kg per week was set'):
        assert plan_page.weekly_rate_value("losing 0.33 kg per week") == "losing 0.33 kg per week"


@allure.feature('Plan page')
@allure.story('Change weekly rate to losing 0.25 kg per week')
def test_change_weekly_rate_losing_250_g(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_5_weekly_rate()
    with allure.step('Verify losing 0.25 kg per week was set'):
        assert plan_page.weekly_rate_value("losing 0.25 kg per week") == "losing 0.25 kg per week"


@allure.feature('Plan page')
@allure.story('Change weekly rate to losing 0.13 kg per week')
def test_change_weekly_rate_losing_130_g(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_6_weekly_rate()
    with allure.step('Verify losing 0.13 kg per week was set'):
        assert plan_page.weekly_rate_value("losing 0.13 kg per week") == "losing 0.13 kg per week"


@allure.feature('Plan page')
@allure.story('Change weekly rate to maintain weight')
def test_change_weekly_rate_maintain_weight(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Enter valid current weight in kb'):
        plan_page.enter_current_weight_kg("55")
    with allure.step('Enter big target weight in kg'):
        plan_page.enter_target_weight("50")
    with allure.step('Enter next year target date'):
        plan_page.enter_next_year_target_date('2024')
    with allure.step('Click change weekly rate radio button'):
        plan_page.change_7_weekly_rate()
    with allure.step('Verify Maintain Weight was set'):
        assert plan_page.weekly_rate_value("Maintain Weight") == "Maintain Weight"


@allure.feature('Plan page')
@allure.story('Open recommendations form')
def test_open_recommendations(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Click on recommend button'):
        plan_page.click_recommend_button()
    with allure.step('Verify recommendations form is displayed'):
        assert plan_page.verify_lose_weight_safely_page_opened() == 'Lose Weight Safely'


@allure.feature('Plan page')
@allure.story('Send Feedback form')
def test_send_feedback_form(driver, auth):
    with allure.step('Open plan page'):
        plan_page = PlanPage(driver)
        plan_page.open_plan_tab()
    with allure.step('Click Send Feedback'):
        plan_page.click_send_feedback_button()
    with allure.step('Verify Send Feedback form is displayed'):
        assert plan_page.is_displayed_feedback_form() == 'We Appreciate Your Feedback'
