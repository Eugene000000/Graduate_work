import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Поиск по названию книги")
class SearchByTitle:

    #Инициализация
    def __init__(self, book_title: str):
        """
        Инициализация объекта для поиска книги по названию
        """
        self.book_title = book_title
    
    @allure.step("Поиск книги по наванию")
    def by_title(self, driver: webdriver.Chrome) -> None:
        """
        Поиск книги по названию
        """

        #Ввод названия книги в поисковую строку
        input_title = driver.find_element(By.NAME, "phrase")
        input_title.send_keys(self.book_title)

        #Нажатие на кнопку ПОИСК
        search = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        search.click()