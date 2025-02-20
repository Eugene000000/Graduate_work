# -
Дипломная работа. Архитектура фреймворка

### - Шаги:
1. Склонировать проект: Выполните команду в терминале: 'git clone https://github.com/Eugene000000/Graduate_work.git

2. Перейти в директорию проекта: cd Final_proj

3. Создать и активировать виртуальное окружение (рекомендуется для управления зависимостями):

4. Установить зависимости: Выполните команду: pip install -r requirements.txt

5. Получение токена: 
 1. Зайти на сайт Читай-город (https://www.chitai-gorod.ru/)
 2. Открыть DevTools (ctrl + shift + i)
 3. Открыть вкладку Application
 4. В строке фильтра написать "access-token" 
 5. Скопировать значение и применить в файле conf.py (Старое значение удалить и применить новое) 

6. Запустить тесты: Запуск с помощью команды pytest tests

### - Стек:
- pytest - основная библиотека для написания и выполнения тестов.
- selenium - библиотека для автоматизации UI тестирования.
- requests - библиотека для работы с HTTP-клиентом, используемая для API тестирования.
- allure - библиотека для генерации отчетов о выполнении тестов.

### - Структура:
- ./tests - тесты API и UI

### - Полезные ссылки:
- [Документация Allure](https://allurereport.org/docs/)
- [Документация pytest](https://docs.pytest.org/en/stable/)
- [Документация Selenium](https://www.selenium.dev/documentation/webdriver/)

### Библеотеки:
Эти команды необходимо прописать

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest
