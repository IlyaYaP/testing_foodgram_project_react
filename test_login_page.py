from pages.log_reg_page import LoginPage
from pages.links import main_page_link
from pages.data_for_registration import ValidDataForRegistration
import pytest
import time


@pytest.mark.registration_form_test(scope='class')
class TestRegistrationForm():

    @pytest.mark.registration_test(scope='function', autouse=True)
    def test_registration_form(self, browser):
        '''Тест регистрации нового пользователя'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.registration_new_user_2(ValidDataForRegistration.valid_data)
        page.alert_handler()
        page.should_be_login_form()

    @pytest.mark.registration_negative_test(scope='function')
    @pytest.mark.parametrize('data', [ValidDataForRegistration.invalid_data_username_email,
                                      ValidDataForRegistration.invalid_data_pass])
    def test_registration_form_negative(self, browser, data):
        '''Тест регистрации нового пользователя'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.registration_new_user_2(data)
        page.is_alert_present()
        page.not_should_be_login_form()


@pytest.mark.login_form_test(scope='class')
class TestLoginForm():

    # Проверка валидных и невалидных данных при аутентификации пользователя
    @pytest.mark.login_test(scope='function')
    def test_login_form(self, browser):
        '''Тест аутентификации нового пользователя'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(ValidDataForRegistration.valid_data_login)
        page.alert_handler()
        page.should_be_create_recipe_button()

    def test_login_form_negative(self, browser):
        '''Тест аутентификации нового пользователя с невалидными данными'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(ValidDataForRegistration.invalid_data_login)
        page.is_alert_present()
        page.not_should_be_create_recipe_button()

    @pytest.mark.password_changes_test(scope='function')
    def test_password_changes(self, browser):
        '''Тест изменения пароля'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(ValidDataForRegistration.valid_data_login)
        page.password_changes()
        page.alert_handler()
        page.should_be_create_recipe_button()
        # Ниже, меняем пароль обратно)
        page.password_changes_back()

    @pytest.mark.negative_login_form(scope='function')
    def test_negative_login_form(self, browser):
        '''Тест формы входа в УЗ'''
        # В данном тесте, воспроизводится сценарий при котором:
        # 1.пользователь при аутентификации, указывает невалидные данные
        # 2.сообщение об ошибке(алерт) не появляется
        # 3.система принимает данные и авторизует пользователя
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(ValidDataForRegistration.invalid_data_login)
        page.is_alert_present()
        page.not_should_be_create_recipe_button()







        