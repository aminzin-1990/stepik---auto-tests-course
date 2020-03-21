import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# вызываем фикстуру в тесте, передав ее как параметр
def test_basket_button(browser):
    browser.get(link)
    # time.sleep(5)  # использовалось для проверки решения (2ой пункт)
    browser.find_element_by_class_name("btn-add-to-basket")
    # проверка длины строки текста на кнопке
    assert len(browser.find_element_by_class_name("btn-add-to-basket").text) > 0
