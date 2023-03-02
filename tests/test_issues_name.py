import allure
from selene.support.shared import browser
from selene import have
from allure_commons.types import Severity


def test_name_issue_with_selene(open_browser_with_size_1920_1080):
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.all('.menu-item').element_by(have.text('Issues')).click()

    browser.element('.codesearch-results').should(have.text('#72'))


def test_name_issue_with_allure_step(open_browser_with_size_1920_1080):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example')
        browser.element('.header-search-input').submit()

    with allure.step('Открываем Issues'):
        browser.all('.menu-item').element_by(have.text('Issues')).click()

    with allure.step('Проверяем наличие Issue с номером'):
        browser.element('.codesearch-results').should(have.text('#72'))


def test_name_issue_allure_step(open_browser_with_size_1920_1080):
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

@allure.step('Проверяем наличие Issue с номером {number}')
def shoild_see_issue_with_number(number):
    browser.element('.codesearch-results').should(have.text(number))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "krivoruchenko_an")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels(open_browser_with_size_1920_1080):
    pass

