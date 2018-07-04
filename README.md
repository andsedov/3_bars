# Ближайшие бары

Скрипт ищет самый большой и самый маленький бар в Москве, а также выводит ближайший к пользователю бар при вводе gps координат.
Список московских баров в формате JSON можно найти по ссылке http://data.mos.ru/opendata/7710881420-bary

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <filepath> # possibly requires call of python3 executive instead of just python
The biggest bar: Спорт бар «Красная машина» with 450 seats
The smallest bar: БАР. СОКИ with 0 seats
Enter longitude: 55.1
Enter latitude: 37.2
The closest bar: ('Бар Виват', 2422.32) meters

```

Запуск на Windows происходит аналогично.

Установка зависимостей:
В файле requirements.txt перечислены используемые в программе зависимости. Установить их можно следующим образом:

```bash

$ pip install -r requirements.txt

```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
