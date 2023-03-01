import allure
from selene.support.shared import browser
from selene import have


def test_name_issue_with_selene():
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.all('.menu-item').element_by(have.text('Issues')).click()

    browser.element('.codesearch-results').should(have.text('#72'))

def test_name_issue_with_lambda_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    open_issues_tab()
    shoild_see_issue_with_number('#72')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repo)
    browser.element('.header-search-input').submit()

@allure.step('Открываем Issues')
def open_issues_tab():
    browser.all('.menu-item').element_by(have.text('Issues')).click()

@allure.step('Проверяем наличик Issue с номером {number}')
def shoild_see_issue_with_number(number):
    browser.element('.codesearch-results').should(have.text(number))

    

