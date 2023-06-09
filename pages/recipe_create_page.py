import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import CreateRecipeLocators


class RecipeCreation(BasePage):

    def create_recipe(self,
                      recipe_name_data,
                      cooking_time_data,
                      recipe_description_data,
                      meal_data,
                      ingredients_data,
                      image_name_data):
        '''Функция создания рецепта'''
        with allure.step('Создаем рецепт.'):
            self.go_to_recipes_creat_page()
            recipe_name = self.browser.find_element(
                        *CreateRecipeLocators.RECIPE_NAME)
            recipe_name.send_keys(recipe_name_data)
            cooking_time = self.browser.find_element(
                        *CreateRecipeLocators.COOKING_TIME)
            cooking_time.send_keys(cooking_time_data)
            recipe_description = self.browser.find_element(
                        *CreateRecipeLocators.RECIPE_DESCRIPTION)
            recipe_description.send_keys(recipe_description_data)
            add_file_button = self.browser.find_element(
                        *CreateRecipeLocators.FILE_INPUT)
            self.tags_selection(meal_data)
            self.add_ingredients(ingredients_data)
            self.add_image(image_name_data, add_file_button)
            button_create_recipe_form = WebDriverWait(
                        self.browser, timeout=1).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[text()="Создать рецепт"]')))
            button_create_recipe_form.click()

    def tags_selection(self, meal):
        '''Функция выбора тега'''
        with allure.step('Выбираем нужный нам тег.'):
            tag_name = self.browser.find_elements(
                       *CreateRecipeLocators.TAG_NAME)
            i = 0
            while i < len(tag_name):
                try:
                    for meal_tag in tag_name:
                        if meal_tag.text == meal:
                            tag_button_locator = (By.XPATH, f'//span[text()="{meal}"]/../button')
                            tag_button = self.browser.find_element(
                                         *tag_button_locator)
                            tag_button.click()
                except IndexError:
                    pass
                i += 1

    def add_ingredients(self, ingredients):
        '''Функция добавления игридиентов'''
        with allure.step('Добавляем индигриенты.'):
            input_ingredients = self.browser.find_element(
                               *CreateRecipeLocators.INGREDIENTS)
            ingredients_amount = self.browser.find_element(
                               *CreateRecipeLocators.AMOUNT_VALUE)
            button_add_ingredients = self.browser.find_element(
                               *CreateRecipeLocators.ADD_INDREDIENT_BUTTON)

            for ingredien, amount in ingredients.items():
                try:
                    input_ingredients.send_keys(ingredien)
                    ingredients_drop_list = WebDriverWait(self.browser,
                                                          timeout=2).until(
                        EC.presence_of_element_located((By.XPATH, f'//div[text()="{ingredien}"]')))
                    ingredients_drop_list.click()
                    ingredients_amount.send_keys(amount)
                    button_add_ingredients.click()
                except StaleElementReferenceException:
                    continue
                else:
                    break

    def should_be_recipe(self, recipe_name):
        '''Проверка наличия созданого рецепта'''
        with allure.step('Проверяем, что наш рецепт создан успешно.'):
            recipe_title = (By.LINK_TEXT, f'{recipe_name}')
            assert self.is_element_present(
                   *recipe_title), 'The created recipe is not presented'
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
