import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from Graduate_work.tests.UI_add_to_cart import AddToCart
from Graduate_work.tests.UI_delete_from_cart import DeleteFromCart
from Graduate_work.tests.UI_search_by_author import SearchByAuthor
from Graduate_work.tests.UI_search_by_title import SearchByTitle
from conf import ui_url

search_by_title = SearchByTitle
search_by_author = SearchByAuthor
delete_from_cart = DeleteFromCart
add_to_cart = AddToCart

@allure.title("Тест поиска книги по названию. Позитивный тест")
@allure.description("Тест служит для проверки функции поиска по названию книги")
@allure.severity("CRITICAL")
def test_search_by_title():
    """
    Тест поиска по названию
    """
    with allure.step("Запустить Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перей на сайт ЧИТАЙ-ГОРОД"):
        driver.get(ui_url)

    with allure.step("Найти книгу по названию БЕРСЕРК"):
        book_title = "Берсерк"
        search_by_title(book_title)

    with allure.step("Получить результаты поиска"):
        result = driver.find_element(By.CLASS_NAME, "product-title__head")

    with allure.step("Проверка успешного поиска"):
        assert result is not None

    with allure.step("Закрыть Chrome"):
        driver.quit()

@allure.title("Тест поиска книг по автору. Позитивный тест")
@allure.description("Тест служит для проверки функции поиска книги по автору")
@allure.severity("CRITICAL")
def test_search_by_author():
        """ 
        Проверка корректности результатов поиска по автору.                
        """
        with allure.step("Запустить Chrome"):
            driver = webdriver.Chrome() 
       
        with allure.step("Перейти на сайт ЧИТАЙ-ГОРОД"):
            driver.get(ui_url)  

        with allure.step("Найти книгу по автору КЭНТАРО МИУРА"):
            author_name = "Кэнтаро Миура"
            search_by_author(author_name)
        
        with allure.step("Получить результаты поиска"):
            results_find = driver.find_element(By.CLASS_NAME, "product-title__author")

        with allure.step("Проверить успешность поиска по автору"):
            assert results_find is not None
    
        with allure.step("Закрыть Chrome"):
            driver.quit()

@allure.title("Тест удаления товара из корзины. Позитивный тест")
@allure.description("Тест служит для проверки корректности удаления товара из корзины")
@allure.severity("BLOCKER")
def test_delete_from_card():
        """
        Проверка корректности удаления товара из корзины.                 
        """

        with allure.step("Запустить Chrome"):
            driver = webdriver.Chrome() 
        
        with allure.step("Перейти на сайт ЧИТАЙ-ГОРОД"):
            driver.get(ui_url)  

        with allure.step("Удалить книгу из корзины"):
            book_title = "Берсерк"
            delete_from_cart(book_title)
            results_del = driver.find_elements(By.CSS_SELECTOR, 'div.product-title__head')

        with allure.step("Проверить отсутствие товара в списке"):
            assert all(book_title not in element.text for element in results_del)

@allure.title("Тест поиска по несуществующему названию. Негативный тест")
@allure.description("Тест служит для проверки возможности найти несуществующую книгу")
@allure.severity("CRITICAL")
def test_mixed_request():
        """
        Проверка отсутствия результата по поиску несуществующего названия книги.
        """
        with allure.step ("Запустить Chrome"):
            driver = webdriver.Chrome() 
       
        with allure.step ("Перейти на сайт ЧИТАЙ-ГОРОД"):
            driver.get(ui_url)  

        with allure.step ("Найти несуществующее название книги"):
            book_title = "fgsgsgssagfgg"
            search_by_title(book_title)

        with allure.step("Проверить отсутствие результатов поиска"):
            results_find = driver.find_elements(By.CSS_SELECTOR, "h4.catalog-empty-result__header") 
            assert results_find is not None
    
        with allure.step("Закрыть Chrome"):
            driver.quit()

@allure.title("Тест поиска по несуществующему автору. Негативный тест")
@allure.description("Тест служит для проверки невозможности найти книгу по несуществующему автору")
@allure.severity("CRITICAL")
def test_wrong_author ():
        """
        Проверка отсутствия результата, поиск по несуществующему автору
        """
    
        with allure.step ("Запустить Chrome"):
            driver = webdriver.Chrome() 
       
        with allure.step ("Перейти на сайт ЧИТАЙ-ГОРОД"):
            driver.get(ui_url)  

        with allure.step ("Найти книгу по несуществующему автору"):
            author_name = "Каьплвадпд"
            search_by_author(author_name)

        with allure.step("Проверить, что поиск не дал результатов"):
            results_find = driver.find_elements(By.CSS_SELECTOR, "h4.catalog-empty-result__header") 
            assert results_find is not None
    
        with allure.step("Закрыть Chrome"):
            driver.quit()