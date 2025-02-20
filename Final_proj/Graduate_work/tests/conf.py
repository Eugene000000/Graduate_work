ui_url = "https://www.chitai-gorod.ru/"
API_url = "https://web-gate.chitai-gorod.ru/api/v2/search/product"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDAxMzQwMDMsImlhdCI6MTczOTk2NjAwMywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjNjM2NkODMxMzY0NGEyYTllYTQ3NjJmZjhiYzEwNGZmNjc2YjIxNWNhNDIyYmI5NGE1NDA0ZmVkM2ZiNTdlOTUiLCJ0eXBlIjoxMH0.HPvCskVqY70A72vAKmCPzv15sMOEdqtc-ilKHu_k5Ik"

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()