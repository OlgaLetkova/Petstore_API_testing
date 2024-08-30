# Petstore_API_testing
## Запуск тестов:
### 1. Через Docker file
* Собрать образ: **docker build -t tests:0.1 .**
* Запустить образ с тестами: **docker run -it --rm tests:0.1 tests**

### 2. Через консоль
Предварительная настройка окружения:

**python3 -m venv venv**

**source venv/bin/activate**    активировать виртуальное окружение

**pip3 install -r requirements.txt**

Запуск:

* **pytest tests**
* С генерацией отчета Allure:

**pytest** путь до теста **alluredir** папка, куда положить json с результатами:

**pytest tests --alluredir allure-results**

Путь до allure-2.29.0 **generate** папка с результатами запуска:

**~/Загрузки/drivers/allure-2.29.0/bin/allure generate allure-results/**

Для повторного запуска **~/Загрузки/drivers/allure-2.29.0/bin/allure generate allure-results/ --clean** с очищением предыдущего результата