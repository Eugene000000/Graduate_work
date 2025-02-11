import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Поиск по автору")
class SearchByAuthor:

    #Инициализация
    def __init__(self, author_name: str):
        """
        Инициализация объекта для поиска по имени автора
        """
        self.author_name = author_name
    @allure.step("Поиск книги по имени автора")
    def by_author(self, driver: webdriver.Chrome) -> None:
        """
        Поиск книги по имени автора
        """
        #Ввод имени автора в строку поиска
        input_author = driver.find_element(By.NAME, "phrase")
        input_author.send_keys(self.author_name)
        
        #Нажатие кнопки ПОИСК
        search = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        search.click()