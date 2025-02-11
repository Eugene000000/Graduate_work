import allure
import requests
from conf import API_url, token

@allure.title("Тест поиск по названию книги")
class pageAPI:
    """
    Класс поиск по названию (API)
    """

    #Базовый UPL
    url = API_url

    #Инициализация
    def __init__(self, url, token):
        """
        Инициализацмя объекта для поиска по названию книги (API)
        """
        self.url = url
        self.token = token

    def _get_header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": token
        }
    
    @allure.step("Поиск по фразе")
    def search_by_phrase_API(self, phrase, customer_city_id=213):
        """
        Поиск продукта по фразе
        """
        
        params = {
            "customerCityId": customer_city_id,
            "phrase": phrase
        }
        resp = requests.get(self.url, headers=self._get_header(),
                            params=params)
        return resp
    
    @allure.step("Поиск названия книги в ответе")
    def search_book_title_in_response(self, response_json):
        """
        Поиск названия книги в ответе
        """

        titles = [book['attributes']['title'] for book in response_json.get(
            'included', []) if book['type'] == 'product']
        allure.attach(str(titles), "Название книги")
        return titles
    
    @allure.step("Поиск автора книги в ответа")
    def search_book_authors_in_response(self, response_json):
        """
        Поиск автора книги в ответе
        """

        book_authors = []
        for book in response_json.get('included', []):
            if book['type'] == 'product':
                authors = book['attributes'].get('authors', [])
                for author in authors:
                    full_name = f"{author.get('firstName', '')} {author.get(
                        'lastName', '')}".strip()
                    book_authors.append(full_name)
        return book_authors