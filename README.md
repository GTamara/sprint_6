# sprint_6

## Установка зависимостей
pip install -r requirements.txt 

## Геренация отчета
pytest tests.py --alluredir=allure_results 
allure serve allure_results

## Геренация актуального requirements.txt
pip freeze > requirements.txt 
