import allure
from screens.ios.main_screen import main_screen


def test_ios_app():
    with allure.step('Click text button'):
        main_screen.click_text_button()
    with allure.step('Input text'):
        main_screen.input_text('Hello world!' + '\n')
    with allure.step('Check output text'):
        output_text = main_screen.get_output_text()
        assert output_text == 'Hello world!'
