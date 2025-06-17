import allure
from allure_commons.types import Severity
from selene import browser, by, have
from model.pages.github import Github

browser.config.window_width = 1920
browser.config.window_height = 1080


def test_issue_name_selene_only():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('khzrx/python_automation_hw_10').submit()
    browser.element(by.link_text('khzrx/python_automation_hw_10')).click()
    browser.element('#issues-tab').click()

    browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text('Issue for test'))


def test_issue_name_with_allure_steps():
    with allure.step('Открыть https://github.com'):
        browser.open('https://github.com')

    with allure.step('Ввести имя репозитория в поле поиска'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('khzrx/python_automation_hw_10').submit()
        browser.element(by.link_text('khzrx/python_automation_hw_10')).click()

    with allure.step('Перейти в найденный репозиторий'):
        browser.element(by.link_text('khzrx/python_automation_hw_10')).click()

    with allure.step('Перейти на вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверить название issue "Issue for test"'):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text('Issue for test'))

def test_issue_name_with_step_decorators():
    github = Github()
    github.open()

    github.search_repo('khzrx/python_automation_hw_10')
    github.go_to_repo('khzrx/python_automation_hw_10')
    github.go_to_issue_tab()

    github.should_have_issue_name('Issue for test')

@allure.tag("smoke")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'fdgoncharenko')
@allure.feature('Issues')
@allure.story('Соответствие названия созданного Issue')
@allure.link('https://github.com', name='Testing')
def test_allure_labels():
    pass