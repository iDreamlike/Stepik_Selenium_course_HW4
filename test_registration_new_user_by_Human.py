from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_registration_new_user(browser):
    browser.find_element(By.ID, "login_link").click()
    browser.find_element(By.ID, "id_registration-email").send_keys("login_15@mail.ru")
    browser.find_element(By.ID, "id_registration-password1").send_keys("Qq111111Qq")
    browser.find_element(By.ID, "id_registration-password2").send_keys("Qq111111Qq")
    browser.find_element(By.NAME, "registration_submit").click()
    try:
        browser.find_element(By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
        result = True
    except NoSuchElementException:
        result = False

    assert result, "Не найдено сообщение об успешной регистрации"
