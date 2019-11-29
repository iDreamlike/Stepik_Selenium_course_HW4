from selenium.common.exceptions import NoSuchElementException


def test_guest_should_see_ButtonAddToBasket_on_product_page(browser):
    browser.find_element_by_css_selector("#browse > li > ul > li:nth-child(1) > a").click()
    browser.find_element_by_css_selector("li:nth-child(3) > .product_pod a").click()
    try:
        browser.find_element_by_css_selector("#add_to_basket_form > button")
        result = True
    except NoSuchElementException:
        result = False

    assert result, "Не найдена кнопка добавления в корзину"


def test_guest_should_adding_product_to_basket(browser):
    browser.find_element_by_css_selector("#browse > li > ul > li:nth-child(1) > a").click()
    browser.find_element_by_css_selector("li:nth-child(3) > .product_pod a").click()
    browser.find_element_by_css_selector("#add_to_basket_form > button").click()
    try:
        browser.find_element_by_css_selector("#messages > .alert-success:nth-child(1)")
        result = True
    except NoSuchElementException:
        result = False

    assert result, "Не найдено сообщение об успешном добавлении товара в корзину"
