import time

from selene.support.shared import browser
from selene import have


def test_name_issue_with_selene():
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.all('.menu-item').element_by(have.text('Issues')).click()

    browser.element('.codesearch-results').should(have.text('#72'))



    

