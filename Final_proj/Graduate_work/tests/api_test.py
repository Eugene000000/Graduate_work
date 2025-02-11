import allure
from Graduate_work.tests.API_search_by_phrase import pageAPI
from conf import API_url 
from conf import token

#Инициализация
page_api = pageAPI

import allure
from Graduate_work.tests.API_search_by_phrase import pageAPI

# Определите базовые данные
url = API_url
token = token

# Инициализация объекта API
api_page = pageAPI(url, token)


@allure.title("Тест поиск книги по названию")
@allure.description("Проверка, что API возвращает книгу с ожидаемым названием")
def test_api_book_by_title():
    response = api_page.search_by_phrase_API("Атака титанов")

    # Проверьте статус ответа
    assert response.status_code == 200, f"Тест провален: статус код {
        response.status_code}."

    expected_title = "Атака титанов"
    response_json = response.json()
    titles = api_page.search_book_title_in_response(response_json)

    assert any(expected_title.lower() in title.lower()
               for title in titles)
    f"Тест провален: название книги '{expected_title}' не найдено в ответе."


@allure.title("Тест поиск книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
def test_api_book_by_author():
    response = api_page.search_by_phrase_API("Хадзимэ Исаяма")

    print("Ответ:", response.text)
    print("Статус код:", response.status_code)

    assert response.status_code == 200, f"Тест провален: статус код {
        response.status_code}."

    expected_author = "Хадзимэ Исаяма"
    response_json = response.json()
    book_authors = api_page.search_book_authors_in_response(response_json)

    assert any(expected_author.lower()
               in author.lower() for author in book_authors), \
        f"Тест провален: автор '{expected_author}' не найден в ответе."


@allure.title("Тест поиск книги по автору на латинице")
@allure.description("Проверка, что API возвращает книгу с названием на латинице.")
def test_api_author_in_english():
    response = api_page.search_by_phrase_API("Lovecraft")

    print("Ответ:", response.text)
    print("Статус код:", response.status_code)

    assert response.status_code == 200, f"Тест провален: статус код {
        response.status_code}."

    expected_title = "Lovecraft"
    response_json = response.json()
    book_titles = api_page.search_book_title_in_response(response_json)

    assert any(expected_title.lower()
               in title.lower() for title in book_titles), \
        f"Тест провален: название книги '{expected_title}' не найдено в ответе"


@allure.title("Тест поиск только спецсимволы")
@allure.description("Проверка, что API возвращает ошибку при поиске только спецсимволов.")
def test_api_Japanese():
    response = api_page.search_by_phrase_API("//--**/--+*")

    assert response.status_code == 422, f"Тест провален: статус код {
        response.status_code}."

    response_json = response.json()
    error = response_json.get('errors', [{}])[0]
    assert error.get('status') == "422", "Тест провален: "
    "ожидаемый статус не найден в ответе."
    assert error.get('title') == "Недопустимая поисковая фраза", "Тест "
    "провален: сообщение об ошибке неверно."


@allure.title("Тест поиск с пустой поисковой строкой")
@allure.description("Проверка, что API возвращает ошибку при пустом поисковом запросе.")
def test_api_empty_search():
    response = api_page.search_by_phrase_API("")
    assert response.status_code == 400, f"Тест провален: статус код {
        response.status_code}."

    response_json = response.json()
    error = response_json.get('errors', [{}])[0]
    assert error.get('status') == "400", "Тест провален: ожидаемый статус "
    "не найден в ответе."
    assert error.get('title') == "Phrase обязательное поле", "Тест провален: "
    "сообщение об ошибке неверно."
