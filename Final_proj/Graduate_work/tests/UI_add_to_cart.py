import allure
from selenium.webdriver.common.by import By
from selenium import webdriver

@allure.title("Добавление товара в карзину")
class AddToCart:

    #Инициализация
    def __init__(self, book_title: str):
        """
        Инициализация объекта для добавлен в корзину.
        """
        self.book_title = book_title

    #Поиск книги по названию
    def book_by_title(self, driver: webdriver.Chrome, book_title: str) -> dict:
        """
        Поиск книги по названию и добавление в корзину
        """
        #Ввод названия книги в строку поиска
        driver.find_element(By.NAME, "phrase").send_keys(book_title)

        #Нажатие на кнопку ПОИСК
        search = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        search.click()

        #Нажатие на кнопку КУПИТЬ
        buy = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Купить']")
        buy.click()

        #Открытие корзины
        cart = driver.find_element(By.CSS_SELECTOR, '.header-cart__icon')
        cart.click()

