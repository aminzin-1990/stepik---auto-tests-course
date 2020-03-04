from selenium import webdriver
import time
import math


# расчет математической функции
def calc(u):
    return str(math.log(abs(12*math.sin(int(u)))))


# ссылка на тестируемый ресурс и запуск вебдрайвера
link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    # поиск и нажатие кнопки
    button_1 = browser.find_element_by_class_name('btn-primary')
    button_1.click()

    # переключение в новое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # расчет и ввод значения
    x = int(browser.find_element_by_id('input_value').text)
    input_value = calc(x)
    input_x = browser.find_element_by_id('answer')
    input_x.send_keys(input_value)

    # поиск и нажатие кнопки
    button_2 = browser.find_element_by_css_selector("button.btn-primary")
    button_2.click()
finally:
    time.sleep(5)
    browser.quit()
