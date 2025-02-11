import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Удаление товара из корзины")
class DeleteFromCart:

    #Инициализация
    def __init__(self, book_title: str):
        """
        Инициализация объекта для удаления из корзины
        """
        self.book_title = book_title

    @allure.step("Поиск книги по название и её удаление из корзины")
    def delete(self, driver: webdriver.Chrome) -> None:
        """
        Поиск книги, добавление в корзину и удаление
        """
        #Поиск книги
        driver.find_element(By.NAME, "phrase").send_keys(self.book_title)

        #Нажатие на кнопку КУПИТЬ
        buy = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Купить']")
        buy.click()

        #Открытие корзины
        cart = driver.find_element(By.CSS_SELECTOR, '.header-cart__icon')
        cart.click()

        #Отчистка корзины
        clear_cart = driver.find_element(By.CSS_SELECTOR, 'span.clear-cart')
        clear_cart.click()