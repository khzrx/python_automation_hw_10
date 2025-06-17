import allure
from selene import browser, by, have


class Github:
    @allure.step('Открыть https://github.com')
    def open(self):
        browser.open('https://github.com')

    @allure.step('Ввести имя репозитория {repo} в поле поиска')
    def search_repo(self, repo):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type(repo).submit()
        browser.element(by.link_text(repo)).click()

    @allure.step('Перейти в найденный репозиторий {repo}')
    def go_to_repo(self, repo):
        browser.element(by.link_text(repo)).click()

    @allure.step('Перейти на вкладку Issues')
    def go_to_issue_tab(self):
        browser.element('#issues-tab').click()

    @allure.step('Проверить название issue {issue_name}')
    def should_have_issue_name(self, issue_name):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text(issue_name))

